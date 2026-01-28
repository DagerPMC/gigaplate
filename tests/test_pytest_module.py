from tests.conftest import (
    assert_all_python_files_valid,
    assert_file_contains,
    assert_file_not_contains,
    assert_files_exist,
    get_pytest_module_files,
)


class TestPytestModule:
    def test_pytest_files_generated(self, generate_project) -> None:
        project = generate_project("myapp", {"pytest"})
        assert_files_exist(project, get_pytest_module_files())

    def test_pytest_python_syntax_valid(self, generate_project) -> None:
        project = generate_project("myapp", {"pytest"})
        assert_all_python_files_valid(project)

    def test_pytest_conftest_basic(self, generate_project) -> None:
        project = generate_project("myapp", {"pytest"})
        conftest = project / "tests" / "conftest.py"

        assert_file_contains(conftest, "setup_test_config")
        assert_file_contains(conftest, "CONFIG_PATH")

    def test_pytest_test_base_exists(self, generate_project) -> None:
        project = generate_project("myapp", {"pytest"})
        test_base = project / "tests" / "test_base.py"

        assert_file_contains(test_base, "def test_example")

    def test_pytest_pyproject_deps(self, generate_project) -> None:
        project = generate_project("myapp", {"pytest"})
        pyproject = project / "pyproject.toml"

        assert_file_contains(pyproject, "pytest>=8.0")
        assert_file_contains(pyproject, "pytest-asyncio>=0.23")

    def test_pytest_taskfile_test_task(self, generate_project) -> None:
        project = generate_project("myapp", {"pytest"})
        taskfile = project / "Taskfile.yaml"

        assert_file_contains(taskfile, "test:")
        assert_file_contains(taskfile, "uv run pytest tests/")

    def test_pytest_no_fastapi_no_test_app(self, generate_project) -> None:
        project = generate_project("myapp", {"pytest"})
        test_app = project / "tests" / "test_app.py"

        assert not test_app.exists()

    def test_pytest_no_fastapi_no_httpx_dep(self, generate_project) -> None:
        project = generate_project("myapp", {"pytest"})
        pyproject = project / "pyproject.toml"

        assert_file_not_contains(pyproject, "httpx")

    def test_pytest_config_test_yaml_empty_base(self, generate_project) -> None:
        project = generate_project("myapp", {"pytest"})
        config = project / "config" / "test.yaml"

        content = config.read_text()
        assert content.strip() == ""
