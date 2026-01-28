from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from gigaplate.modules import AVAILABLE_MODULES, MODULE_REGISTRY
from gigaplate.modules.base import BaseModule


class Generator:
    def __init__(self, name: str, output_dir: Path, modules: set[str]) -> None:
        self.name = name
        self.output_dir = output_dir
        self.modules = modules
        self.project_path = output_dir / name

        templates_dir = Path(__file__).parent / "templates"
        self.env = Environment(
            loader=FileSystemLoader(templates_dir),
            keep_trailing_newline=True,
            trim_blocks=True,
            lstrip_blocks=True,
        )

        self.context = {
            "name": name,
            "modules": modules,
            **{f"has_{m}": m in modules for m in AVAILABLE_MODULES},
        }

        self._generated_files: dict[str, str] = {}

    def generate(self) -> None:
        self.project_path.mkdir(parents=True, exist_ok=True)

        base_module = BaseModule(self)
        base_module.generate()

        for module_name in self.modules:
            if module_cls := MODULE_REGISTRY.get(module_name):
                module_cls(self).generate()

        self._handle_interactions()
        self._write_files()

    def _handle_interactions(self) -> None:
        if self.context["has_fastapi"] and self.context["has_sqlalchemy"]:
            self._handle_fastapi_sqlalchemy()

        if self.context["has_aiogram"] and self.context["has_sqlalchemy"]:
            self._handle_aiogram_sqlalchemy()

        if self.context["has_sqlalchemy"] and self.context["has_redis"]:
            self._handle_sqlalchemy_redis()

    def _handle_fastapi_sqlalchemy(self) -> None:
        template = self.env.get_template("fastapi/controllers/dependencies.py.j2")
        self.add_file(f"{self.name}/controllers/dependencies.py", template.render(**self.context))

    def _handle_aiogram_sqlalchemy(self) -> None:
        session_template = self.env.get_template("aiogram/middlewares/session.py.j2")
        self.add_file(f"{self.name}/middlewares/session.py", session_template.render(**self.context))

        user_template = self.env.get_template("aiogram/middlewares/user.py.j2")
        self.add_file(f"{self.name}/middlewares/user.py", user_template.render(**self.context))

        user_model_template = self.env.get_template("aiogram/db/models/user.py.j2")
        self.add_file(f"{self.name}/db/models/user.py", user_model_template.render(**self.context))

        bl_init_template = self.env.get_template("aiogram/bl/__init__.py.j2")
        self.add_file(f"{self.name}/bl/__init__.py", bl_init_template.render(**self.context))

        bl_user_template = self.env.get_template("aiogram/bl/user.py.j2")
        self.add_file(f"{self.name}/bl/user.py", bl_user_template.render(**self.context))

        main_template = self.env.get_template("aiogram/main_with_sqlalchemy.py.j2")
        self.add_file(f"{self.name}/main.py", main_template.render(**self.context))

    def _handle_sqlalchemy_redis(self) -> None:
        new_files: dict[str, str] = {}
        files_to_remove: list[str] = []

        for filepath, content in self._generated_files.items():
            db_prefix = f"{self.name}/db/"
            is_in_db = filepath.startswith(db_prefix)
            is_already_reorganized = (
                filepath.startswith(f"{self.name}/db/sql/")
                or filepath.startswith(f"{self.name}/db/redis/")
            )
            if is_in_db and not is_already_reorganized:
                if "redis" in filepath:
                    new_path = filepath.replace(f"{self.name}/db/", f"{self.name}/db/redis/")
                else:
                    new_path = filepath.replace(f"{self.name}/db/", f"{self.name}/db/sql/")
                new_files[new_path] = content
                files_to_remove.append(filepath)

        for filepath in files_to_remove:
            del self._generated_files[filepath]

        self._generated_files.update(new_files)

        db_init_template = self.env.get_template("sqlalchemy/db/__init__combined.py.j2")
        self.add_file(f"{self.name}/db/__init__.py", db_init_template.render(**self.context))

    def _write_files(self) -> None:
        for filepath, content in self._generated_files.items():
            full_path = self.project_path / filepath
            full_path.parent.mkdir(parents=True, exist_ok=True)
            full_path.write_text(content)

    def add_file(self, path: str, content: str) -> None:
        self._generated_files[path] = content

    def remove_file(self, path: str) -> None:
        self._generated_files.pop(path, None)
