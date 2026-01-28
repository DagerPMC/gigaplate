from gigaplate.modules._base import Module


class AiogramModule(Module):
    def generate(self) -> None:
        self.add_template("aiogram/main.py.j2", f"{self.name}/main.py")
        self.add_template("aiogram/controllers/__init__.py.j2", f"{self.name}/controllers/__init__.py")
        self.add_template("aiogram/controllers/router.py.j2", f"{self.name}/controllers/router.py")
        self.add_template("aiogram/middlewares/__init__.py.j2", f"{self.name}/middlewares/__init__.py")
        self.add_template("aiogram/middlewares/throttling.py.j2", f"{self.name}/middlewares/throttling.py")
