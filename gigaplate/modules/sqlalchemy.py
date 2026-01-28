from gigaplate.modules._base import Module


class SQLAlchemyModule(Module):
    def generate(self) -> None:
        self.add_template("sqlalchemy/alembic.ini.j2", "alembic.ini")
        self.add_template("sqlalchemy/migrations/env.py.j2", "migrations/env.py")
        self.add_template("sqlalchemy/migrations/script.py.mako.j2", "migrations/script.py.mako")
        self.add_file("migrations/versions/.gitkeep", "")

        self.add_template("sqlalchemy/db/__init__.py.j2", f"{self.name}/db/__init__.py")
        self.add_template("sqlalchemy/db/base.py.j2", f"{self.name}/db/base.py")
        self.add_template("sqlalchemy/db/types.py.j2", f"{self.name}/db/types.py")
        self.add_template("sqlalchemy/db/mixin.py.j2", f"{self.name}/db/mixin.py")
        self.add_template("sqlalchemy/db/models/__init__.py.j2", f"{self.name}/db/models/__init__.py")
        self.add_template("sqlalchemy/db/utils/__init__.py.j2", f"{self.name}/db/utils/__init__.py")
        self.add_template("sqlalchemy/db/utils/session.py.j2", f"{self.name}/db/utils/session.py")

        ext_sa = f"{self.name}/ext/sqlalchemy"
        self.add_template("sqlalchemy_ext/ext/__init__.py.j2", f"{self.name}/ext/__init__.py")
        self.add_template("sqlalchemy_ext/ext/sqlalchemy/__init__.py.j2", f"{ext_sa}/__init__.py")
        self.add_template("sqlalchemy_ext/ext/sqlalchemy/transactional.py.j2", f"{ext_sa}/transactional.py")
        self.add_template("sqlalchemy_ext/ext/sqlalchemy/lazy.py.j2", f"{ext_sa}/lazy.py")
