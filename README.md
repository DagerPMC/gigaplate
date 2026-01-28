# Gigaplate

[![PyPI version](https://img.shields.io/pypi/v/gigaplate)](https://pypi.org/project/gigaplate/)

Python project template generator with modular architecture.

## Installation

```bash
pip install gigaplate
# or
pipx install gigaplate
# or
uv tool install gigaplate
```

## Usage

```bash
# Base project only
gigaplate my_project

# With FastAPI
gigaplate my_project --fastapi

# FastAPI + SQLAlchemy + Redis
gigaplate my_project --fastapi --sqlalchemy --redis

# Aiogram bot with database
gigaplate my_project --aiogram --sqlalchemy --redis

# Using short flags
gigaplate my_project -f -s -r

# Using comma-separated list
gigaplate my_project -- fastapi,sqlalchemy,redis
```

## Available Modules

| Module | Flag | Description |
|--------|------|-------------|
| FastAPI | `--fastapi`, `-f` | REST API with FastAPI |
| SQLAlchemy | `--sqlalchemy`, `-s` | Async SQLAlchemy + Alembic |
| Redis | `--redis`, `-r` | Redis connection |
| Aiogram | `--aiogram`, `-a` | Telegram bot with aiogram |
| CLI | `--cli`, `-c` | Click CLI interface |

## Module Interactions

- **FastAPI + SQLAlchemy**: Adds session dependency injection
- **Aiogram + SQLAlchemy**: Adds session/user middlewares, user model
- **SQLAlchemy + Redis**: Reorganizes db folder (`db/sql/`, `db/redis/`)
- **FastAPI + Aiogram**: Not allowed (mutually exclusive)

## Generated Project Structure

```
my_project/
├── my_project/
│   ├── __init__.py
│   ├── config.py
│   ├── main.py / app.py
│   ├── controllers/
│   ├── middlewares/
│   ├── db/
│   └── utils/
├── config/
├── migrations/          # if sqlalchemy
├── Taskfile.yaml
├── docker-compose.yaml
├── pyproject.toml
└── CLAUDE.md
```

## License

MIT
