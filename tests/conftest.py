import ast
from collections.abc import Callable
from pathlib import Path

import pytest

from gigaplate.generator import Generator


@pytest.fixture
def generate_project(tmp_path: Path) -> Callable[[str, set[str]], Path]:
    def _generate(name: str, modules: set[str] | None = None) -> Path:
        if modules is None:
            modules = set()
        generator = Generator(name=name, output_dir=tmp_path, modules=modules)
        generator.generate()
        return tmp_path / name

    return _generate


def assert_files_exist(project_path: Path, expected_files: list[str]) -> None:
    for file_path in expected_files:
        full_path = project_path / file_path
        assert full_path.exists(), f"Expected file {file_path} does not exist"


def assert_files_not_exist(project_path: Path, unexpected_files: list[str]) -> None:
    for file_path in unexpected_files:
        full_path = project_path / file_path
        assert not full_path.exists(), f"Unexpected file {file_path} exists"


def assert_python_syntax_valid(file_path: Path) -> None:
    content = file_path.read_text()
    try:
        ast.parse(content)
    except SyntaxError as e:
        pytest.fail(f"Syntax error in {file_path}: {e}")


def assert_file_contains(file_path: Path, substring: str) -> None:
    content = file_path.read_text()
    assert substring in content, f"Expected '{substring}' not found in {file_path}"


def assert_file_not_contains(file_path: Path, substring: str) -> None:
    content = file_path.read_text()
    assert substring not in content, f"Unexpected '{substring}' found in {file_path}"


def assert_all_python_files_valid(project_path: Path) -> None:
    for py_file in project_path.rglob("*.py"):
        assert_python_syntax_valid(py_file)


# Common file list helpers
BASE_FILES = [
    ".gitignore",
    ".dockerignore",
    "Dockerfile",
    "docker-compose.yaml",
    "Taskfile.yaml",
    "ruff.toml",
    "mypy.ini",
    "pyproject.toml",
    "CLAUDE.md",
    "AGENTS.md",
    "config/local.yaml",
    "config/local.yaml.example",
]


def base_src_files(name: str) -> list[str]:
    return [
        f"{name}/__init__.py",
        f"{name}/config.py",
        f"{name}/utils/__init__.py",
        f"{name}/utils/setup.py",
    ]


def fastapi_files(name: str) -> list[str]:
    return [
        f"{name}/app.py",
        f"{name}/controllers/__init__.py",
        f"{name}/controllers/router.py",
        f"{name}/controllers/api/__init__.py",
        f"{name}/controllers/healthcheck.py",
        f"{name}/middlewares/__init__.py",
        f"{name}/middlewares/logging.py",
    ]


def sqlalchemy_files(name: str, *, reorganized: bool = False) -> list[str]:
    prefix = f"{name}/db/sql" if reorganized else f"{name}/db"
    return [
        "alembic.ini",
        "migrations/env.py",
        "migrations/script.py.mako",
        "migrations/versions/.gitkeep",
        f"{name}/db/__init__.py",
        f"{prefix}/base.py",
        f"{prefix}/types.py",
        f"{prefix}/mixin.py",
        f"{prefix}/models/__init__.py",
        f"{prefix}/utils/__init__.py",
        f"{prefix}/utils/session.py",
        f"{name}/ext/__init__.py",
        f"{name}/ext/sqlalchemy/__init__.py",
        f"{name}/ext/sqlalchemy/transactional.py",
        f"{name}/ext/sqlalchemy/lazy.py",
    ]


def redis_files(name: str, *, reorganized: bool = False) -> list[str]:
    if reorganized:
        return [f"{name}/db/redis/redis.py"]
    return [f"{name}/db/redis.py"]


def aiogram_files(name: str) -> list[str]:
    return [
        f"{name}/main.py",
        f"{name}/controllers/__init__.py",
        f"{name}/controllers/router.py",
        f"{name}/middlewares/__init__.py",
        f"{name}/middlewares/throttling.py",
    ]


def aiogram_sqlalchemy_files(name: str, *, reorganized: bool = False) -> list[str]:
    db_prefix = f"{name}/db/sql" if reorganized else f"{name}/db"
    return [
        f"{name}/middlewares/session.py",
        f"{name}/middlewares/user.py",
        f"{db_prefix}/models/user.py",
        f"{name}/bl/__init__.py",
        f"{name}/bl/user.py",
    ]


def cli_files(name: str) -> list[str]:
    return [
        f"{name}/__main__.py",
        f"{name}/cli.py",
    ]


def get_pytest_module_files() -> list[str]:
    return [
        "tests/__init__.py",
        "tests/test_base.py",
        "tests/conftest.py",
        "config/test.yaml",
    ]
