from gigaplate.modules._base import Module


class FastAPIModule(Module):
    def generate(self) -> None:
        self.add_template("fastapi/app.py.j2", f"{self.name}/app.py")
        self.add_template("fastapi/controllers/__init__.py.j2", f"{self.name}/controllers/__init__.py")
        self.add_template("fastapi/controllers/router.py.j2", f"{self.name}/controllers/router.py")
        self.add_template("fastapi/controllers/api/__init__.py.j2", f"{self.name}/controllers/api/__init__.py")
        self.add_template("fastapi/controllers/healthcheck.py.j2", f"{self.name}/controllers/healthcheck.py")
        self.add_template("fastapi/middlewares/__init__.py.j2", f"{self.name}/middlewares/__init__.py")
        self.add_template("fastapi/middlewares/logging.py.j2", f"{self.name}/middlewares/logging.py")

        self.generator.remove_file(f"{self.name}/main.py")
