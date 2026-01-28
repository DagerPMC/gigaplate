from tests.conftest import (
    BASE_FILES,
    aiogram_files,
    assert_all_python_files_valid,
    assert_file_contains,
    assert_files_exist,
    assert_files_not_exist,
    base_src_files,
)


class TestAiogramModule:
    def test_aiogram_files_generated(self, generate_project) -> None:
        project = generate_project("myapp", {"aiogram"})
        assert_files_exist(project, aiogram_files("myapp"))

    def test_aiogram_no_fastapi_files(self, generate_project) -> None:
        project = generate_project("myapp", {"aiogram"})

        unexpected_files = [
            "myapp/app.py",
            "myapp/middlewares/logging.py",
            "myapp/controllers/api/__init__.py",
        ]

        assert_files_not_exist(project, unexpected_files)

    def test_aiogram_no_sqlalchemy_files(self, generate_project) -> None:
        project = generate_project("myapp", {"aiogram"})

        unexpected_files = [
            "alembic.ini",
            "myapp/db/__init__.py",
            "myapp/middlewares/session.py",
            "myapp/middlewares/user.py",
            "myapp/bl/__init__.py",
        ]

        assert_files_not_exist(project, unexpected_files)

    def test_aiogram_python_syntax_valid(self, generate_project) -> None:
        project = generate_project("myapp", {"aiogram"})
        assert_all_python_files_valid(project)

    def test_aiogram_main_has_bot_imports(self, generate_project) -> None:
        project = generate_project("myapp", {"aiogram"})
        main_file = project / "myapp" / "main.py"
        assert_file_contains(main_file, "aiogram")

    def test_aiogram_router_exists(self, generate_project) -> None:
        project = generate_project("myapp", {"aiogram"})
        router_file = project / "myapp" / "controllers" / "router.py"
        assert_file_contains(router_file, "Router")

    def test_aiogram_throttling_middleware(self, generate_project) -> None:
        project = generate_project("myapp", {"aiogram"})
        throttling_file = project / "myapp" / "middlewares" / "throttling.py"
        assert_file_contains(throttling_file, "Throttling")

    def test_aiogram_base_files_present(self, generate_project) -> None:
        project = generate_project("myapp", {"aiogram"})
        assert_files_exist(project, [*BASE_FILES, *base_src_files("myapp")])
