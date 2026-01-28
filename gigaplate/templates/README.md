# Templates

Jinja2 templates for project generation. Each subfolder corresponds to a module.

## Structure

```
templates/
├── base/           # Always included
├── fastapi/        # --fastapi flag
├── sqlalchemy/     # --sqlalchemy flag
├── sqlalchemy_ext/ # Included with sqlalchemy
├── redis/          # --redis flag
├── aiogram/        # --aiogram flag
└── cli/            # --cli flag
```

## Template Variables

All templates receive these context variables:

| Variable | Type | Description |
|----------|------|-------------|
| `name` | str | Project name |
| `modules` | set[str] | Enabled module names |
| `has_fastapi` | bool | FastAPI enabled |
| `has_sqlalchemy` | bool | SQLAlchemy enabled |
| `has_redis` | bool | Redis enabled |
| `has_aiogram` | bool | Aiogram enabled |
| `has_cli` | bool | CLI enabled |

## Jinja2 Settings

```python
Environment(
    loader=FileSystemLoader(templates_dir),
    keep_trailing_newline=True,
    trim_blocks=True,
    lstrip_blocks=True,
)
```

- `keep_trailing_newline` - preserves final newline in files
- `trim_blocks` - removes first newline after block tags
- `lstrip_blocks` - strips leading whitespace before block tags

## Module Interactions

### FastAPI + SQLAlchemy
- Generates `controllers/dependencies.py`
- `app.py` imports session initialization

### Aiogram + SQLAlchemy
- Uses `main_with_sqlalchemy.py.j2` instead of `main.py.j2`
- Generates session/user middlewares
- Generates User model and business logic

### SQLAlchemy + Redis
- Reorganizes folder structure:
  - `db/*.py` → `db/sql/*.py`
  - `db/redis.py` → `db/redis/redis.py`
- Uses `db/__init__combined.py.j2`

## Adding New Templates

1. Create template file with `.j2` extension
2. Use Jinja2 syntax for conditionals/variables
3. Register in corresponding module's `generate()` method:

```python
def generate(self) -> None:
    self.add_template("module/file.py.j2", f"{self.name}/file.py")
```

## Notes

- README.md files in template folders are documentation only
- They are NOT copied to generated projects
- Only files explicitly registered via `add_template()` are included
