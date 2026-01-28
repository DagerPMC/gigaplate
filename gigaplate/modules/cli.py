from gigaplate.modules._base import Module


class CliModule(Module):
    def generate(self) -> None:
        self.add_template("cli/__main__.py.j2", f"{self.name}/__main__.py")
        self.add_template("cli/cli.py.j2", f"{self.name}/cli.py")
