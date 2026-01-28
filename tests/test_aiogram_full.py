from tests.conftest import (
    BASE_FILES,
    aiogram_files,
    aiogram_sqlalchemy_files,
    assert_all_python_files_valid,
    assert_file_contains,
    assert_files_exist,
    assert_files_not_exist,
    base_src_files,
    cli_files,
    redis_files,
    sqlalchemy_files,
)


class TestAiogramFullCombination:
    """Test Aiogram + SQLAlchemy + Redis + CLI combination."""

    def test_all_expected_files_generated(self, generate_project) -> None:
        project = generate_project("myapp", {"aiogram", "sqlalchemy", "redis", "cli"})

        expected_files = [
            *BASE_FILES,
            *base_src_files("myapp"),
            *aiogram_files("myapp"),
            *aiogram_sqlalchemy_files("myapp", reorganized=True),
            *sqlalchemy_files("myapp", reorganized=True),
            *redis_files("myapp", reorganized=True),
            *cli_files("myapp"),
        ]

        assert_files_exist(project, expected_files)

    def test_no_old_db_structure(self, generate_project) -> None:
        project = generate_project("myapp", {"aiogram", "sqlalchemy", "redis", "cli"})

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
        project = generate_project("myapp", {"aiogram", "sqlalchemy", "redis", "cli"})
        assert_all_python_files_valid(project)

    def test_main_has_aiogram(self, generate_project) -> None:
        project = generate_project("myapp", {"aiogram", "sqlalchemy", "redis", "cli"})
        main_file = project / "myapp" / "main.py"
        assert_file_contains(main_file, "aiogram")

    def test_session_middleware_exists(self, generate_project) -> None:
        project = generate_project("myapp", {"aiogram", "sqlalchemy", "redis", "cli"})
        session_file = project / "myapp" / "middlewares" / "session.py"
        assert_file_contains(session_file, "session")

    def test_user_middleware_exists(self, generate_project) -> None:
        project = generate_project("myapp", {"aiogram", "sqlalchemy", "redis", "cli"})
        user_file = project / "myapp" / "middlewares" / "user.py"
        assert_file_contains(user_file, "user")

    def test_bl_user_exists(self, generate_project) -> None:
        project = generate_project("myapp", {"aiogram", "sqlalchemy", "redis", "cli"})
        bl_user_file = project / "myapp" / "bl" / "user.py"
        assert_file_contains(bl_user_file, "user")

    def test_db_init_imports_sql(self, generate_project) -> None:
        project = generate_project("myapp", {"aiogram", "sqlalchemy", "redis", "cli"})
        db_init = project / "myapp" / "db" / "__init__.py"
        assert_file_contains(db_init, "sql")

    def test_cli_has_click(self, generate_project) -> None:
        project = generate_project("myapp", {"aiogram", "sqlalchemy", "redis", "cli"})
        cli_file = project / "myapp" / "cli.py"
        assert_file_contains(cli_file, "click")

    def test_no_fastapi_files(self, generate_project) -> None:
        project = generate_project("myapp", {"aiogram", "sqlalchemy", "redis", "cli"})

        unexpected_files = [
            "myapp/app.py",
            "myapp/middlewares/logging.py",
            "myapp/controllers/api/__init__.py",
            "myapp/controllers/dependencies.py",
        ]

        assert_files_not_exist(project, unexpected_files)
