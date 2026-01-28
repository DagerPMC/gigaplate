# SQLAlchemy Templates

Async SQLAlchemy with Alembic migrations.

## Files

| Template | Output | Description |
|----------|--------|-------------|
| `alembic.ini.j2` | `alembic.ini` | Alembic configuration |
| `migrations/env.py.j2` | `migrations/env.py` | Migration environment |
| `migrations/script.py.mako.j2` | `migrations/script.py.mako` | Migration template |
| `db/__init__.py.j2` | `{name}/db/__init__.py` | DB package exports |
| `db/__init__combined.py.j2` | `{name}/db/__init__.py` | DB init when combined with redis |
| `db/base.py.j2` | `{name}/db/base.py` | DeclarativeBase with type mappings |
| `db/types.py.j2` | `{name}/db/types.py` | Custom column types |
| `db/mixin.py.j2` | `{name}/db/mixin.py` | Timestamp mixins |
| `db/models/__init__.py.j2` | `{name}/db/models/__init__.py` | Models package |
| `db/utils/__init__.py.j2` | `{name}/db/utils/__init__.py` | Utils package |
| `db/utils/session.py.j2` | `{name}/db/utils/session.py` | Session management |

## Custom Types (`types.py`)

Pre-defined annotated types for models:
- `int_pk` - Integer primary key
- `uuid_pk` - UUID primary key (using uuid7)
- `str50` - String(50)
- `str255` - String(255)

## Mixins (`mixin.py`)

Reusable model mixins:
- `CreatedAtMixin` - `created_at` with server default `now()`
- `UpdatedAtMixin` - `updated_at` with server default and onupdate

## Session Management (`session.py`)

Context-var based session handling:
- `s.session` - current AsyncSession (via ContextVar)
- `s.session_transaction` - current nested transaction
- `s.maker` - async_sessionmaker instance
- `init_session()` - creates engine and sessionmaker

Engine settings:
- Uses `asyncpg` driver
- `isolation_level="AUTOCOMMIT"` (transactions managed explicitly)

## Folder Reorganization

When combined with Redis (`has_redis`), the db structure changes:
- `db/` files move to `db/sql/`
- Uses `__init__combined.py.j2` for `db/__init__.py`
- Allows `db/redis/` to coexist

## Usage in Models

```python
from {name}.db.base import Base
from {name}.db.types import uuid_pk, str255
from {name}.db.mixin import CreatedAtMixin

class User(Base, CreatedAtMixin):
    __tablename__ = "users"

    id: Mapped[uuid_pk]
    name: Mapped[str255]
```
