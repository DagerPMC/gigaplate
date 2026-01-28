from gigaplate.modules._base import Module


class BaseModule(Module):
    def generate(self) -> None:
        self.add_template("base/gitignore.j2", ".gitignore")
        self.add_template("base/dockerignore.j2", ".dockerignore")
        self.add_template("base/Dockerfile.j2", "Dockerfile")
        self.add_template("base/docker-compose.yaml.j2", "docker-compose.yaml")
        self.add_template("base/Taskfile.yaml.j2", "Taskfile.yaml")
        self.add_template("base/ruff.toml.j2", "ruff.toml")
        self.add_template("base/mypy.ini.j2", "mypy.ini")
        self.add_template("base/pyproject.toml.j2", "pyproject.toml")
        self.add_template("base/CLAUDE.md.j2", "CLAUDE.md")

        self.add_template("base/config/local.yaml.j2", "config/local.yaml")
        self.add_template("base/config/local.yaml.example.j2", "config/local.yaml.example")

        self.add_template("base/src/__init__.py.j2", f"{self.name}/__init__.py")
        self.add_template("base/src/config.py.j2", f"{self.name}/config.py")
        self.add_template("base/src/utils/__init__.py.j2", f"{self.name}/utils/__init__.py")
        self.add_template("base/src/utils/setup.py.j2", f"{self.name}/utils/setup.py")

        if not self.context["has_fastapi"] and not self.context["has_aiogram"]:
            self.add_template("base/src/main.py.j2", f"{self.name}/main.py")
