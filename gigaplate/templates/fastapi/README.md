# FastAPI Templates

REST API structure using FastAPI framework.

## Files

| Template | Output | Description |
|----------|--------|-------------|
| `app.py.j2` | `{name}/app.py` | FastAPI application with lifespan |
| `controllers/__init__.py.j2` | `{name}/controllers/__init__.py` | Controllers package |
| `controllers/router.py.j2` | `{name}/controllers/router.py` | Main router aggregator |
| `controllers/api/__init__.py.j2` | `{name}/controllers/api/__init__.py` | API routes package |
| `controllers/healthcheck.py.j2` | `{name}/controllers/healthcheck.py` | Health check endpoint |
| `controllers/dependencies.py.j2` | `{name}/controllers/dependencies.py` | DI dependencies (only with sqlalchemy) |
| `middlewares/__init__.py.j2` | `{name}/middlewares/__init__.py` | Middlewares package |
| `middlewares/logging.py.j2` | `{name}/middlewares/logging.py` | Request logging middleware |

## Application Structure (`app.py`)

- Uses `asynccontextmanager` lifespan for startup/shutdown
- Lifespan initializes:
  - `init_config()` - always
  - `init_session()` - if sqlalchemy enabled
  - `init_redis()` - if redis enabled
- Includes `LoggingMiddleware`
- Mounts main router

## Conditional Imports

The `app.py` template adjusts imports based on module combination:

```python
# sqlalchemy + redis
from {name}.db.sql.utils.session import init_session
from {name}.db.redis.redis import init_redis

# sqlalchemy only
from {name}.db.utils.session import init_session

# redis only (no sqlalchemy)
from {name}.db.redis import init_redis
```

## Dependencies (`dependencies.py`)

Only generated when `has_sqlalchemy` is true. Provides:
- `SessionDep` - typed dependency for async session injection
- Session management via context manager

## Module Behavior

- Removes `main.py` from base module (replaces with `app.py`)
- Run with: `uvicorn {name}.app:app --reload`
