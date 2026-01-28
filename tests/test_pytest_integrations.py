from tests.conftest import (
    assert_all_python_files_valid,
    assert_file_contains,
    assert_files_exist,
)


class TestPytestWithFastAPI:
    def test_pytest_fastapi_test_app_generated(self, generate_project) -> None:
        project = generate_project("myapp", {"pytest", "fastapi"})

        expected_files = [
            "tests/__init__.py",
            "tests/test_base.py",
            "tests/conftest.py",
            "tests/test_app.py",
            "config/test.yaml",
        ]

        assert_files_exist(project, expected_files)

    def test_pytest_fastapi_python_syntax_valid(self, generate_project) -> None:
        project = generate_project("myapp", {"pytest", "fastapi"})
        assert_all_python_files_valid(project)

    def test_pytest_fastapi_conftest_client(self, generate_project) -> None:
        project = generate_project("myapp", {"pytest", "fastapi"})
        conftest = project / "tests" / "conftest.py"

        assert_file_contains(conftest, "AsyncClient")
        assert_file_contains(conftest, "client")
        assert_file_contains(conftest, "ASGITransport")

    def test_pytest_fastapi_test_app_tests(self, generate_project) -> None:
        project = generate_project("myapp", {"pytest", "fastapi"})
        test_app = project / "tests" / "test_app.py"

        assert_file_contains(test_app, "test_health_check_returns_ok")
        assert_file_contains(test_app, "test_openapi_schema_accessible")

    def test_pytest_fastapi_httpx_dep(self, generate_project) -> None:
        project = generate_project("myapp", {"pytest", "fastapi"})
        pyproject = project / "pyproject.toml"

        assert_file_contains(pyproject, "httpx>=0.27")

    def test_fastapi_healthcheck_generated(self, generate_project) -> None:
        project = generate_project("myapp", {"fastapi"})
        healthcheck = project / "myapp" / "controllers" / "healthcheck.py"

        assert healthcheck.exists()
        assert_file_contains(healthcheck, "/health")
        assert_file_contains(healthcheck, '"status": "ok"')

    def test_fastapi_app_includes_healthcheck(self, generate_project) -> None:
        project = generate_project("myapp", {"fastapi"})
        app = project / "myapp" / "app.py"

        assert_file_contains(app, "from myapp.controllers.healthcheck import router as health_router")
        assert_file_contains(app, "app.include_router(health_router)")


class TestPytestWithSQLAlchemy:
    def test_pytest_sqlalchemy_conftest_fixtures(self, generate_project) -> None:
        project = generate_project("myapp", {"pytest", "sqlalchemy"})
        conftest = project / "tests" / "conftest.py"

        assert_file_contains(conftest, "_run_migrations")
        assert_file_contains(conftest, "session")
        assert_file_contains(conftest, "AlembicConfig")

    def test_pytest_sqlalchemy_config_test_yaml(self, generate_project) -> None:
        project = generate_project("myapp", {"pytest", "sqlalchemy"})
        config = project / "config" / "test.yaml"

        assert_file_contains(config, "database_dsn")
        assert_file_contains(config, "myapp_test")
        assert_file_contains(config, "5433")

    def test_pytest_sqlalchemy_docker_compose_test_db(self, generate_project) -> None:
        project = generate_project("myapp", {"pytest", "sqlalchemy"})
        compose = project / "docker-compose.yaml"

        assert_file_contains(compose, "postgres-test:")
        assert_file_contains(compose, "5433:5432")
        assert_file_contains(compose, "myapp_test")

    def test_pytest_sqlalchemy_python_syntax_valid(self, generate_project) -> None:
        project = generate_project("myapp", {"pytest", "sqlalchemy"})
        assert_all_python_files_valid(project)


class TestPytestWithRedis:
    def test_pytest_redis_conftest_fixture(self, generate_project) -> None:
        project = generate_project("myapp", {"pytest", "redis"})
        conftest = project / "tests" / "conftest.py"

        assert_file_contains(conftest, "redis_client")
        assert_file_contains(conftest, "flushdb")

    def test_pytest_redis_config_test_yaml(self, generate_project) -> None:
        project = generate_project("myapp", {"pytest", "redis"})
        config = project / "config" / "test.yaml"

        assert_file_contains(config, "redis:")
        assert_file_contains(config, "port: 6380")

    def test_pytest_redis_docker_compose_test_redis(self, generate_project) -> None:
        project = generate_project("myapp", {"pytest", "redis"})
        compose = project / "docker-compose.yaml"

        assert_file_contains(compose, "redis-test:")
        assert_file_contains(compose, "6380:6379")

    def test_pytest_redis_python_syntax_valid(self, generate_project) -> None:
        project = generate_project("myapp", {"pytest", "redis"})
        assert_all_python_files_valid(project)


class TestPytestWithAiogram:
    def test_pytest_aiogram_config_test_yaml(self, generate_project) -> None:
        project = generate_project("myapp", {"pytest", "aiogram"})
        config = project / "config" / "test.yaml"

        assert_file_contains(config, "token: \"TEST_BOT_TOKEN\"")
        assert_file_contains(config, "updates_strategy: \"polling\"")

    def test_pytest_aiogram_python_syntax_valid(self, generate_project) -> None:
        project = generate_project("myapp", {"pytest", "aiogram"})
        assert_all_python_files_valid(project)


class TestPytestFullStack:
    def test_pytest_fastapi_sqlalchemy_redis(self, generate_project) -> None:
        project = generate_project("myapp", {"pytest", "fastapi", "sqlalchemy", "redis"})
        assert_all_python_files_valid(project)

        conftest = project / "tests" / "conftest.py"
        assert_file_contains(conftest, "client")
        assert_file_contains(conftest, "session")
        assert_file_contains(conftest, "redis_client")
        assert_file_contains(conftest, "from myapp.db.sql.utils.session")
        assert_file_contains(conftest, "from myapp.db.redis.redis")

    def test_pytest_aiogram_sqlalchemy_redis(self, generate_project) -> None:
        project = generate_project("myapp", {"pytest", "aiogram", "sqlalchemy", "redis"})
        assert_all_python_files_valid(project)

        conftest = project / "tests" / "conftest.py"
        assert_file_contains(conftest, "session")
        assert_file_contains(conftest, "redis_client")
