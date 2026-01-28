# Pytest Module Templates

This module provides test infrastructure for generated projects.

## Files Generated

- `tests/__init__.py` - Package init (empty)
- `tests/test_base.py` - Basic passing test
- `tests/conftest.py` - Pytest fixtures (conditional based on modules)
- `tests/test_app.py` - FastAPI tests (only with `has_fastapi`)
- `config/test.yaml` - Test configuration

## Fixtures

### Always Available
- `setup_test_config` - Session-scoped, sets CONFIG_PATH to test.yaml

### With FastAPI (`has_fastapi`)
- `client` - AsyncClient for testing FastAPI app

### With SQLAlchemy (`has_sqlalchemy`)
- `_run_migrations` - Session-scoped, runs migrations on setup, downgrades on teardown
- `session` - Function-scoped AsyncSession with automatic rollback

### With Redis (`has_redis`)
- `redis_client` - Async Redis client with flushdb cleanup

## Template Variables

- `name` - Project name
- `has_fastapi` - FastAPI module enabled
- `has_sqlalchemy` - SQLAlchemy module enabled
- `has_redis` - Redis module enabled
- `has_aiogram` - Aiogram module enabled
