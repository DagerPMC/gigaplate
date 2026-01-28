from tests.conftest import (
    BASE_FILES,
    assert_all_python_files_valid,
    assert_file_contains,
    assert_files_exist,
    assert_files_not_exist,
    base_src_files,
)


class TestBaseModule:
    def test_base_files_generated(self, generate_project) -> None:
        project = generate_project("myapp")

        expected_files = [
            *BASE_FILES,
            *base_src_files("myapp"),
            "myapp/main.py",
        ]

        assert_files_exist(project, expected_files)

    def test_base_no_extra_files(self, generate_project) -> None:
        project = generate_project("myapp")

        unexpected_files = [
            "myapp/app.py",
            "myapp/controllers/__init__.py",
            "myapp/middleware/__init__.py",
            "myapp/middlewares/__init__.py",
            "alembic.ini",
            "myapp/db/__init__.py",
            "myapp/cli.py",
            "myapp/__main__.py",
        ]

        assert_files_not_exist(project, unexpected_files)

    def test_base_python_syntax_valid(self, generate_project) -> None:
        project = generate_project("myapp")
        assert_all_python_files_valid(project)

    def test_base_pyproject_has_project_name(self, generate_project) -> None:
        project = generate_project("myapp")
        assert_file_contains(project / "pyproject.toml", 'name = "myapp"')

    def test_base_config_imports(self, generate_project) -> None:
        project = generate_project("myapp")
        config_file = project / "myapp" / "config.py"
        assert_file_contains(config_file, "from pathlib import Path")
