from gigaplate.modules._base import Module
from gigaplate.modules.aiogram import AiogramModule
from gigaplate.modules.cli import CliModule
from gigaplate.modules.fastapi import FastAPIModule
from gigaplate.modules.pytest import PytestModule
from gigaplate.modules.redis import RedisModule
from gigaplate.modules.sqlalchemy import SQLAlchemyModule

MODULE_REGISTRY: dict[str, type[Module]] = {
    "fastapi": FastAPIModule,
    "sqlalchemy": SQLAlchemyModule,
    "redis": RedisModule,
    "aiogram": AiogramModule,
    "cli": CliModule,
    "pytest": PytestModule,
}

AVAILABLE_MODULES = frozenset(MODULE_REGISTRY.keys())

__all__ = [
    "Module",
    "MODULE_REGISTRY",
    "AVAILABLE_MODULES",
    "AiogramModule",
    "CliModule",
    "FastAPIModule",
    "PytestModule",
    "RedisModule",
    "SQLAlchemyModule",
]
