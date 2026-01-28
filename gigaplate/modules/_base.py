from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gigaplate.generator import Generator


class Module(ABC):
    def __init__(self, generator: Generator) -> None:
        self.generator = generator
        self.env = generator.env
        self.context = generator.context
        self.name = generator.name

    @abstractmethod
    def generate(self) -> None:
        ...

    def render_template(self, template_path: str) -> str:
        template = self.env.get_template(template_path)
        return template.render(**self.context)

    def add_file(self, path: str, content: str) -> None:
        self.generator.add_file(path, content)

    def add_template(self, template_path: str, output_path: str) -> None:
        content = self.render_template(template_path)
        self.add_file(output_path, content)
