# Base Templates

Core project structure generated for every project.

## Files

| Template | Output | Description |
|----------|--------|-------------|
| `gitignore.j2` | `.gitignore` | Python/IDE ignores |
| `dockerignore.j2` | `.dockerignore` | Docker build ignores |
| `Dockerfile.j2` | `Dockerfile` | Multi-stage Python build |
| `docker-compose.yaml.j2` | `docker-compose.yaml` | Services (conditionally includes postgres, redis) |
| `Taskfile.yaml.j2` | `Taskfile.yaml` | Task runner commands |
| `ruff.toml.j2` | `ruff.toml` | Ruff linter config (line-length: 80) |
| `mypy.ini.j2` | `mypy.ini` | Mypy strict config |
| `pyproject.toml.j2` | `pyproject.toml` | Project metadata with conditional dependencies |
| `CLAUDE.md.j2` | `CLAUDE.md` | AI assistant instructions |
| `AGENTS.md.j2` | `AGENTS.md` | Multi-agent coordination |
| `config/local.yaml.j2` | `config/local.yaml` | Local config file |
| `config/local.yaml.example.j2` | `config/local.yaml.example` | Config template |
| `src/__init__.py.j2` | `{name}/__init__.py` | Package init |
| `src/config.py.j2` | `{name}/config.py` | Pydantic config loader |
| `src/main.py.j2` | `{name}/main.py` | Entry point (only if no fastapi/aiogram) |
| `src/utils/__init__.py.j2` | `{name}/utils/__init__.py` | Utils package |
| `src/utils/setup.py.j2` | `{name}/utils/setup.py` | Initialization helpers |

## Config System (`config.py`)

- Uses Pydantic BaseModel for validation
- Loads from YAML file (`config/local.yaml`)
- Supports `CONFIG_PATH` env variable
- Conditional sections based on modules:
  - `has_fastapi`: AppModel (host, port, debug)
  - `has_sqlalchemy`: database_dsn
  - `has_redis`: RedisModel (host, port, db, url property)
  - `has_aiogram`: token, updates_strategy

## Template Variables

All base templates have access to:
- `name` - project name
- `has_fastapi` - bool
- `has_sqlalchemy` - bool
- `has_redis` - bool
- `has_aiogram` - bool
- `has_cli` - bool

## Conditional Logic

- `main.py` is only generated if neither FastAPI nor Aiogram is enabled
- `docker-compose.yaml` includes postgres service if `has_sqlalchemy`
- `docker-compose.yaml` includes redis service if `has_redis`
- `pyproject.toml` dependencies vary by enabled modules
