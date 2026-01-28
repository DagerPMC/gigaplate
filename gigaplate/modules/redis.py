from gigaplate.modules._base import Module


class RedisModule(Module):
    def generate(self) -> None:
        self.add_template("redis/db/redis.py.j2", f"{self.name}/db/redis.py")
