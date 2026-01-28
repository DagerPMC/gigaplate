from gigaplate.modules._base import Module


class PytestModule(Module):
    def generate(self) -> None:
        self.add_template("pytest/tests/__init__.py.j2", "tests/__init__.py")
        self.add_template("pytest/tests/test_base.py.j2", "tests/test_base.py")
        self.add_template("pytest/tests/conftest.py.j2", "tests/conftest.py")
        self.add_template("pytest/config/test.yaml.j2", "config/test.yaml")

        if self.context["has_fastapi"]:
            self.add_template("pytest/tests/test_app.py.j2", "tests/test_app.py")
