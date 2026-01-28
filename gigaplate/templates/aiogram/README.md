# Aiogram Templates

Telegram bot structure using aiogram 3.x.

## Files

### Core Files
| Template | Output | Description |
|----------|--------|-------------|
| `main.py.j2` | `{name}/main.py` | Bot entry point (basic) |
| `main_with_sqlalchemy.py.j2` | `{name}/main.py` | Bot entry point (with DB) |
| `controllers/__init__.py.j2` | `{name}/controllers/__init__.py` | Handlers package |
| `controllers/router.py.j2` | `{name}/controllers/router.py` | Main router |

### Middlewares
| Template | Output | Description |
|----------|--------|-------------|
| `middlewares/__init__.py.j2` | `{name}/middlewares/__init__.py` | Middleware package |
| `middlewares/throttling.py.j2` | `{name}/middlewares/throttling.py` | Rate limiting |
| `middlewares/session.py.j2` | `{name}/middlewares/session.py` | DB session (with sqlalchemy) |
| `middlewares/user.py.j2` | `{name}/middlewares/user.py` | User loading (with sqlalchemy) |

### SQLAlchemy Integration
| Template | Output | Description |
|----------|--------|-------------|
| `db/models/user.py.j2` | `{name}/db/models/user.py` | User model |
| `bl/__init__.py.j2` | `{name}/bl/__init__.py` | Business logic package |
| `bl/user.py.j2` | `{name}/bl/user.py` | User operations |

## Main Entry Point

### Basic (`main.py.j2`)
- Initializes config
- Creates Bot and Dispatcher
- Registers ThrottlingMiddleware
- Starts polling

### With SQLAlchemy (`main_with_sqlalchemy.py.j2`)
Additionally:
- Initializes database session
- Registers SessionMiddleware, UserMiddleware
- Manages session lifecycle per update

## Throttling Middleware

Rate limiter with LRU-style cleanup:

```python
ThrottlingMiddleware(rate_limit=0.5, max_users=500)
```

- `rate_limit` - minimum seconds between messages per user
- `max_users` - max tracked users before cleanup
- Silently drops messages that exceed rate limit
- Only applies to Message events

## SQLAlchemy Integration

When `has_sqlalchemy` is true:

### Session Middleware
- Creates new session per update
- Sets `s.session` context var
- Commits on success, rollbacks on error

### User Middleware
- Loads or creates User from `event.from_user.id`
- Injects `user` into handler data
- Uses `bl.user.get_or_create_user()`

### User Model
Basic user model with telegram_id:
```python
class User(Base, CreatedAtMixin, UpdatedAtMixin):
    __tablename__ = "users"

    id: Mapped[uuid_pk]
    telegram_id: Mapped[int] = mapped_column(unique=True, index=True)
```

### Business Logic (`bl/user.py`)
```python
async def get_or_create_user(telegram_id: int) -> User:
    # Returns existing or creates new user
```

## Updates Strategy

Configured via `config.updates_strategy`:
- `"polling"` - long polling
- Other values raise `ValueError` (webhook support not implemented)
