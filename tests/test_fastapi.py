from tests.conftest import (
    BASE_FILES,
    assert_all_python_files_valid,
    assert_file_contains,
    assert_files_exist,
    assert_files_not_exist,
    base_src_files,
    fastapi_files,
)


class TestFastAPIModule:
    def test_fastapi_files_generated(self, generate_project) -> None:
        project = generate_project("myapp", {"fastapi"})
        assert_files_exist(project, fastapi_files("myapp"))

    def test_fastapi_removes_main_py(self, generate_project) -> None:
        project = generate_project("myapp", {"fastapi"})
        assert_files_not_exist(project, ["myapp/main.py"])

    def test_fastapi_no_sqlalchemy_files(self, generate_project) -> None:
        project = generate_project("myapp", {"fastapi"})

        unexpected_files = [
            "alembic.ini",
            "myapp/db/__init__.py",
            "myapp/controllers/dependencies.py",
        ]

        assert_files_not_exist(project, unexpected_files)

    def test_fastapi_python_syntax_valid(self, generate_project) -> None:
        project = generate_project("myapp", {"fastapi"})
        assert_all_python_files_valid(project)

    def test_fastapi_app_imports(self, generate_project) -> None:
        project = generate_project("myapp", {"fastapi"})
        app_file = project / "myapp" / "app.py"
        assert_file_contains(app_file, "from fastapi import FastAPI")

    def test_fastapi_router_exists(self, generate_project) -> None:
        project = generate_project("myapp", {"fastapi"})
        router_file = project / "myapp" / "controllers" / "router.py"
        assert_file_contains(router_file, "APIRouter")

    def test_fastapi_base_files_present(self, generate_project) -> None:
        project = generate_project("myapp", {"fastapi"})
        assert_files_exist(project, [*BASE_FILES, *base_src_files("myapp")])
