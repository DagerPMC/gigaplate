# Redis Templates

Async Redis connection using `redis-py`.

## Files

| Template | Output | Description |
|----------|--------|-------------|
| `db/__init__.py.j2` | `{name}/db/__init__.py` | DB package init (only without sqlalchemy) |
| `db/redis/__init__.py.j2` | `{name}/db/redis/__init__.py` | Redis package init (only with sqlalchemy) |
| `db/redis.py.j2` | `{name}/db/redis.py` or `{name}/db/redis/redis.py` | Redis connection manager |

## Redis Manager (`redis.py`)

Context-var based Redis client:

```python
from {name}.db.redis import r, init_redis

# Initialize (usually in lifespan/startup)
init_redis()

# Use anywhere
await r.redis.set("key", "value")
value = await r.redis.get("key")
```

### Features

- `r.redis` - current Redis client (via ContextVar)
- `init_redis()` - creates/reuses connection from pool
- Connection pooling by DSN (reuses existing connections)
- Auto-decodes responses to UTF-8 strings

### Connection Settings

Reads from config:
```yaml
redis:
  host: localhost
  port: 6379
  db: 0
```

URL format: `redis://{host}:{port}/{db}`

## Folder Structure

### Redis Only
```
{name}/
└── db/
    ├── __init__.py
    └── redis.py
```

### With SQLAlchemy
When combined with SQLAlchemy, folder is reorganized:
```
{name}/
└── db/
    ├── __init__.py
    ├── sql/
    │   ├── base.py
    │   ├── models/
    │   └── utils/
    └── redis/
        └── redis.py
```

Import paths change accordingly:
- Redis only: `from {name}.db.redis import r`
- With SQLAlchemy: `from {name}.db.redis.redis import r`
