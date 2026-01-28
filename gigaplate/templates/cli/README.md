# CLI Templates

Click-based command line interface.

## Files

| Template | Output | Description |
|----------|--------|-------------|
| `__main__.py.j2` | `{name}/__main__.py` | Module entry point |
| `cli.py.j2` | `{name}/cli.py` | Click CLI definition |

## Module Entry (`__main__.py`)

Allows running as module:
```bash
python -m {name}
```

Simply imports and calls the CLI:
```python
from {name}.cli import cli

if __name__ == "__main__":
    cli()
```

## CLI Definition (`cli.py`)

Basic Click group with config initialization:

```python
import click
from {name}.utils.setup import init_config

@click.group()
def cli() -> None:
    init_config()
```

### Extending

Add commands by decorating with `@cli.command()`:

```python
@cli.command()
@click.argument("name")
def greet(name: str) -> None:
    click.echo(f"Hello, {name}!")
```

Add subgroups:

```python
@cli.group()
def db() -> None:
    """Database commands."""
    pass

@db.command()
def migrate() -> None:
    """Run migrations."""
    pass
```

## Usage

```bash
# Via module
python -m {name}

# Via entry point (if configured in pyproject.toml)
{name}

# With commands
{name} greet World
{name} db migrate
```

## Dependencies

Adds `click>=8.0` to project dependencies in `pyproject.toml`.
