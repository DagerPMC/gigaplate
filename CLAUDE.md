# Gigaplate - Python Project Template Generator

## Overview
CLI tool that generates modular Python project templates based on common patterns.

## Project Structure
```
gigaplate/
├── gigaplate/           # Main package
│   ├── cli.py          # Click CLI interface
│   ├── generator.py    # Main generator logic
│   ├── modules/        # Template modules
│       ├── base.py     # BaseModule class
│       ├── base_module.py  # Base project module
│       ├── fastapi.py  # FastAPI module
│       ├── sqlalchemy.py   # SQLAlchemy module
│       ├── redis.py    # Redis module
│       ├── aiogram.py  # Aiogram module
│       └── cli_module.py   # CLI module
├── templates/          # Jinja2 templates
│   ├── base/          # Base project templates
│   ├── fastapi/       # FastAPI templates
│   ├── sqlalchemy/    # SQLAlchemy templates
│   ├── redis/         # Redis templates
│   ├── aiogram/       # Aiogram templates
│   └── cli/           # CLI templates
└── config/            # Local config

## Commands
- `task run` - Run gigaplate
- `task lint` - Run linters
- `task format` - Format code
- `task test` - Generate test projects

## Usage
```bash
gigaplate my_project                    # Base only
gigaplate my_project --fastapi          # With FastAPI
gigaplate my_project -f -s              # FastAPI + SQLAlchemy
gigaplate my_project -- fastapi,redis   # Using comma-separated list
```

## Module Dependencies
- FastAPI + Aiogram: PROHIBITED (mutually exclusive)
- FastAPI + SQLAlchemy: Adds session dependency
- Aiogram + SQLAlchemy: Adds session/user middlewares
- SQLAlchemy + Redis: Reorganizes db folder structure
