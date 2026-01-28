from tests.conftest import (
    BASE_FILES,
    assert_all_python_files_valid,
    assert_file_contains,
    assert_files_exist,
    assert_files_not_exist,
    base_src_files,
    redis_files,
)


class TestRedisModule:
    def test_redis_files_generated(self, generate_project) -> None:
        project = generate_project("myapp", {"redis"})
        assert_files_exist(project, redis_files("myapp"))

    def test_redis_no_sqlalchemy_files(self, generate_project) -> None:
        project = generate_project("myapp", {"redis"})

        unexpected_files = [
            "alembic.ini",
            "myapp/db/base.py",
            "myapp/db/models/__init__.py",
            "myapp/db/sql/__init__.py",
            "myapp/db/redis/redis.py",
        ]

        assert_files_not_exist(project, unexpected_files)

    def test_redis_python_syntax_valid(self, generate_project) -> None:
        project = generate_project("myapp", {"redis"})
        assert_all_python_files_valid(project)

    def test_redis_file_has_redis_import(self, generate_project) -> None:
        project = generate_project("myapp", {"redis"})
        redis_file = project / "myapp" / "db" / "redis.py"
        assert_file_contains(redis_file, "redis")

    def test_redis_has_main_py(self, generate_project) -> None:
        project = generate_project("myapp", {"redis"})
        assert_files_exist(project, ["myapp/main.py"])

    def test_redis_base_files_present(self, generate_project) -> None:
        project = generate_project("myapp", {"redis"})
        assert_files_exist(project, [*BASE_FILES, *base_src_files("myapp")])
