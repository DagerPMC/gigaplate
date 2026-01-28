from tests.conftest import (
    BASE_FILES,
    assert_all_python_files_valid,
    assert_file_contains,
    assert_files_exist,
    assert_files_not_exist,
    base_src_files,
    cli_files,
    fastapi_files,
    redis_files,
    sqlalchemy_files,
)


class TestFastAPIFullCombination:
    """Test FastAPI + SQLAlchemy + Redis + CLI combination."""

    def test_all_expected_files_generated(self, generate_project) -> None:
        project = generate_project("myapp", {"fastapi", "sqlalchemy", "redis", "cli"})

        expected_files = [
            *BASE_FILES,
            *base_src_files("myapp"),
            *fastapi_files("myapp"),
            "myapp/controllers/dependencies.py",  # FastAPI + SQLAlchemy integration
            *sqlalchemy_files("myapp", reorganized=True),
            *redis_files("myapp", reorganized=True),
            *cli_files("myapp"),
        ]

        assert_files_exist(project, expected_files)

    def test_no_main_py(self, generate_project) -> None:
        project = generate_project("myapp", {"fastapi", "sqlalchemy", "redis", "cli"})
        assert_files_not_exist(project, ["myapp/main.py"])

    def test_no_old_db_structure(self, generate_project) -> None:
        project = generate_project("myapp", {"fastapi", "sqlalchemy", "redis", "cli"})

        unexpected_files = [
            "myapp/db/base.py",
            "myapp/db/types.py",
            "myapp/db/mixin.py",
            "myapp/db/models/__init__.py",
            "myapp/db/utils/__init__.py",
            "myapp/db/utils/session.py",
            "myapp/db/redis.py",
        ]

        assert_files_not_exist(project, unexpected_files)

    def test_all_python_syntax_valid(self, generate_project) -> None:
        project = generate_project("myapp", {"fastapi", "sqlalchemy", "redis", "cli"})
        assert_all_python_files_valid(project)

    def test_app_imports_fastapi(self, generate_project) -> None:
        project = generate_project("myapp", {"fastapi", "sqlalchemy", "redis", "cli"})
        app_file = project / "myapp" / "app.py"
        assert_file_contains(app_file, "from fastapi import FastAPI")

    def test_dependencies_has_session(self, generate_project) -> None:
        project = generate_project("myapp", {"fastapi", "sqlalchemy", "redis", "cli"})
        deps_file = project / "myapp" / "controllers" / "dependencies.py"
        assert_file_contains(deps_file, "session")

    def test_db_init_imports_sql(self, generate_project) -> None:
        project = generate_project("myapp", {"fastapi", "sqlalchemy", "redis", "cli"})
        db_init = project / "myapp" / "db" / "__init__.py"
        assert_file_contains(db_init, "sql")

    def test_cli_has_click(self, generate_project) -> None:
        project = generate_project("myapp", {"fastapi", "sqlalchemy", "redis", "cli"})
        cli_file = project / "myapp" / "cli.py"
        assert_file_contains(cli_file, "click")

    def test_no_aiogram_files(self, generate_project) -> None:
        project = generate_project("myapp", {"fastapi", "sqlalchemy", "redis", "cli"})

        unexpected_files = [
            "myapp/middlewares/throttling.py",
            "myapp/middlewares/session.py",
            "myapp/middlewares/user.py",
            "myapp/bl/__init__.py",
            "myapp/bl/user.py",
        ]

        assert_files_not_exist(project, unexpected_files)
