from tests.conftest import (
    BASE_FILES,
    assert_all_python_files_valid,
    assert_file_contains,
    assert_files_exist,
    assert_files_not_exist,
    base_src_files,
    sqlalchemy_files,
)


class TestSQLAlchemyModule:
    def test_sqlalchemy_files_generated(self, generate_project) -> None:
        project = generate_project("myapp", {"sqlalchemy"})
        assert_files_exist(project, sqlalchemy_files("myapp"))

    def test_sqlalchemy_no_redis_files(self, generate_project) -> None:
        project = generate_project("myapp", {"sqlalchemy"})

        unexpected_files = [
            "myapp/db/redis.py",
            "myapp/db/sql/__init__.py",
            "myapp/db/redis/redis.py",
        ]

        assert_files_not_exist(project, unexpected_files)

    def test_sqlalchemy_python_syntax_valid(self, generate_project) -> None:
        project = generate_project("myapp", {"sqlalchemy"})
        assert_all_python_files_valid(project)

    def test_sqlalchemy_base_has_correct_imports(self, generate_project) -> None:
        project = generate_project("myapp", {"sqlalchemy"})
        base_file = project / "myapp" / "db" / "base.py"
        assert_file_contains(base_file, "from sqlalchemy")

    def test_sqlalchemy_session_has_async_session(self, generate_project) -> None:
        project = generate_project("myapp", {"sqlalchemy"})
        session_file = project / "myapp" / "db" / "utils" / "session.py"
        assert_file_contains(session_file, "AsyncSession")

    def test_sqlalchemy_has_main_py(self, generate_project) -> None:
        project = generate_project("myapp", {"sqlalchemy"})
        assert_files_exist(project, ["myapp/main.py"])

    def test_sqlalchemy_base_files_present(self, generate_project) -> None:
        project = generate_project("myapp", {"sqlalchemy"})
        assert_files_exist(project, [*BASE_FILES, *base_src_files("myapp")])
