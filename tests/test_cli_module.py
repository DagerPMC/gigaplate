from tests.conftest import (
    BASE_FILES,
    assert_all_python_files_valid,
    assert_file_contains,
    assert_files_exist,
    base_src_files,
    cli_files,
)


class TestCliModule:
    def test_cli_files_generated(self, generate_project) -> None:
        project = generate_project("myapp", {"cli"})
        assert_files_exist(project, cli_files("myapp"))

    def test_cli_python_syntax_valid(self, generate_project) -> None:
        project = generate_project("myapp", {"cli"})
        assert_all_python_files_valid(project)

    def test_cli_has_click_import(self, generate_project) -> None:
        project = generate_project("myapp", {"cli"})
        cli_file = project / "myapp" / "cli.py"
        assert_file_contains(cli_file, "click")

    def test_cli_main_module_runs_cli(self, generate_project) -> None:
        project = generate_project("myapp", {"cli"})
        main_file = project / "myapp" / "__main__.py"
        assert_file_contains(main_file, "cli")

    def test_cli_has_main_py(self, generate_project) -> None:
        project = generate_project("myapp", {"cli"})
        assert_files_exist(project, ["myapp/main.py"])

    def test_cli_base_files_present(self, generate_project) -> None:
        project = generate_project("myapp", {"cli"})
        assert_files_exist(project, [*BASE_FILES, *base_src_files("myapp")])
