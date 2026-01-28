from gigaplate.modules._base import Module


class RedisModule(Module):
    def generate(self) -> None:
        if self.context["has_sqlalchemy"]:
            self.add_template("redis/db/redis/__init__.py.j2", f"{self.name}/db/redis/__init__.py")
            self.add_template("redis/db/redis.py.j2", f"{self.name}/db/redis/redis.py")
        else:
            self.add_template("redis/db/__init__.py.j2", f"{self.name}/db/__init__.py")
            self.add_template("redis/db/redis.py.j2", f"{self.name}/db/redis.py")
