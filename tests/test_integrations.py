from tests.conftest import (
    assert_all_python_files_valid,
    assert_file_contains,
    assert_files_exist,
    assert_files_not_exist,
)


class TestFastAPISQLAlchemyIntegration:
    def test_dependencies_file_generated(self, generate_project) -> None:
        project = generate_project("myapp", {"fastapi", "sqlalchemy"})
        assert_files_exist(project, ["myapp/controllers/dependencies.py"])

    def test_dependencies_has_session_import(self, generate_project) -> None:
        project = generate_project("myapp", {"fastapi", "sqlalchemy"})
        deps_file = project / "myapp" / "controllers" / "dependencies.py"
        assert_file_contains(deps_file, "session")

    def test_all_python_syntax_valid(self, generate_project) -> None:
        project = generate_project("myapp", {"fastapi", "sqlalchemy"})
        assert_all_python_files_valid(project)

    def test_no_main_py(self, generate_project) -> None:
        project = generate_project("myapp", {"fastapi", "sqlalchemy"})
        assert_files_not_exist(project, ["myapp/main.py"])


class TestAiogramSQLAlchemyIntegration:
    def test_session_middleware_generated(self, generate_project) -> None:
        project = generate_project("myapp", {"aiogram", "sqlalchemy"})
        assert_files_exist(project, ["myapp/middlewares/session.py"])

    def test_user_middleware_generated(self, generate_project) -> None:
        project = generate_project("myapp", {"aiogram", "sqlalchemy"})
        assert_files_exist(project, ["myapp/middlewares/user.py"])

    def test_user_model_generated(self, generate_project) -> None:
        project = generate_project("myapp", {"aiogram", "sqlalchemy"})
        assert_files_exist(project, ["myapp/db/models/user.py"])

    def test_bl_user_generated(self, generate_project) -> None:
        project = generate_project("myapp", {"aiogram", "sqlalchemy"})

        expected_files = [
            "myapp/bl/__init__.py",
            "myapp/bl/user.py",
        ]

        assert_files_exist(project, expected_files)

    def test_session_middleware_imports(self, generate_project) -> None:
        project = generate_project("myapp", {"aiogram", "sqlalchemy"})
        session_file = project / "myapp" / "middlewares" / "session.py"
        assert_file_contains(session_file, "session")

    def test_all_python_syntax_valid(self, generate_project) -> None:
        project = generate_project("myapp", {"aiogram", "sqlalchemy"})
        assert_all_python_files_valid(project)


class TestSQLAlchemyRedisIntegration:
    def test_db_folder_reorganized(self, generate_project) -> None:
        project = generate_project("myapp", {"sqlalchemy", "redis"})

        expected_files = [
            "myapp/db/__init__.py",
            "myapp/db/sql/__init__.py",
            "myapp/db/sql/base.py",
            "myapp/db/sql/types.py",
            "myapp/db/sql/mixin.py",
            "myapp/db/sql/models/__init__.py",
            "myapp/db/sql/utils/__init__.py",
            "myapp/db/sql/utils/session.py",
            "myapp/db/redis/redis.py",
        ]

        assert_files_exist(project, expected_files)

    def test_old_db_structure_removed(self, generate_project) -> None:
        project = generate_project("myapp", {"sqlalchemy", "redis"})

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

    def test_db_init_imports_from_sql(self, generate_project) -> None:
        project = generate_project("myapp", {"sqlalchemy", "redis"})
        db_init = project / "myapp" / "db" / "__init__.py"
        assert_file_contains(db_init, "sql")

    def test_all_python_syntax_valid(self, generate_project) -> None:
        project = generate_project("myapp", {"sqlalchemy", "redis"})
        assert_all_python_files_valid(project)

    def test_has_main_py(self, generate_project) -> None:
        project = generate_project("myapp", {"sqlalchemy", "redis"})
        assert_files_exist(project, ["myapp/main.py"])
