from pathlib import Path

import click

from gigaplate.generator import Generator


@click.command()
@click.argument("name")
@click.option("--fastapi", "-f", is_flag=True, help="Add FastAPI module")
@click.option("--sqlalchemy", "-s", is_flag=True, help="Add SQLAlchemy module")
@click.option("--redis", "-r", is_flag=True, help="Add Redis module")
@click.option("--aiogram", "-a", is_flag=True, help="Add Aiogram module")
@click.option("--cli", "-c", is_flag=True, help="Add CLI module")
@click.option("--pytest", "-t", is_flag=True, help="Add Pytest module")
@click.option("--output", "-o", type=click.Path(), default=None, help="Output directory")
@click.argument("modules", nargs=-1)
def cli(
    name: str,
    fastapi: bool,
    sqlalchemy: bool,
    redis: bool,
    aiogram: bool,
    cli: bool,
    pytest: bool,
    output: str | None,
    modules: tuple[str, ...],
) -> None:
    flag_values = {
        "fastapi": fastapi,
        "sqlalchemy": sqlalchemy,
        "redis": redis,
        "aiogram": aiogram,
        "cli": cli,
        "pytest": pytest,
    }
    selected_modules = {name for name, enabled in flag_values.items() if enabled}

    for module_arg in modules:
        for module in module_arg.split(","):
            module = module.strip().lower()
            if module:
                selected_modules.add(module)

    if "fastapi" in selected_modules and "aiogram" in selected_modules:
        raise click.ClickException("FastAPI and Aiogram modules are mutually exclusive")

    output_dir = Path(output) if output else Path.cwd().parent
    project_path = output_dir / name

    if project_path.exists():
        raise click.ClickException(f"Directory already exists: {project_path}")

    generator = Generator(
        name=name,
        output_dir=output_dir,
        modules=selected_modules,
    )

    generator.generate()

    click.echo(f"Project created at: {project_path}")
    click.echo(f"Modules: {', '.join(sorted(selected_modules)) or 'base only'}")
