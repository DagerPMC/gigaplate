# SQLAlchemy Extensions

Advanced SQLAlchemy utilities for transaction management and lazy loading.

## Files

| Template | Output | Description |
|----------|--------|-------------|
| `ext/__init__.py.j2` | `{name}/ext/__init__.py` | Extensions package |
| `ext/sqlalchemy/__init__.py.j2` | `{name}/ext/sqlalchemy/__init__.py` | SQLAlchemy ext package |
| `ext/sqlalchemy/transactional.py.j2` | `{name}/ext/sqlalchemy/transactional.py` | Transaction decorator |
| `ext/sqlalchemy/lazy.py.j2` | `{name}/ext/sqlalchemy/lazy.py` | Lazy relation loader |

## Transactional Decorator (`transactional.py`)

Decorator for explicit transaction management with isolation levels.

### Isolation Levels

```python
class IsolationLevel(IntEnum):
    AUTOCOMMIT = 1
    READ_COMMITTED = 2
    REPEATABLE_READ = 3
    SERIALIZABLE = 4
```

### Usage

```python
from {name}.ext.sqlalchemy import transactional, IsolationLevel

@transactional
async def create_user(name: str) -> User:
    # runs in READ_COMMITTED by default
    ...

@transactional(isolation_level=IsolationLevel.SERIALIZABLE)
async def transfer_funds(from_id: int, to_id: int, amount: int):
    # runs in SERIALIZABLE
    ...
```

### Features

- Automatic commit on success
- Automatic rollback on exception
- Nested transaction support (savepoints)
- Isolation level consistency checking (nested can't be stricter than outer)
- Cleans up transaction state in `finally` block

## Lazy Relation Loader (`lazy.py`)

Decorator for on-demand relationship loading.

### Usage

```python
from {name}.ext.sqlalchemy import lazy

class User(Base):
    posts: Mapped[list["Post"]] = relationship()

@lazy("posts")
async def get_posts(user: User) -> list[Post]:
    return user.posts

# Usage
user = await get_user(1)  # posts not loaded
posts = await get_posts(user)  # loads posts if unloaded
```

### Features

- Checks if relation is already loaded via `inspect(model).unloaded`
- Uses `selectinload` strategy by default (configurable)
- Supports additional query options as varargs
- Works with string relation names or relation attributes

## Conditional Imports

Templates adjust imports based on redis presence:
- With redis: imports from `db.sql.utils.session`
- Without redis: imports from `db.utils.session`
