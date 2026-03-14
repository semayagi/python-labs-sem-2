from typing import Iterable

from src.models.task import Task


class GeneratorTaskSource:
    """
    Генерирует задачи программно
    """

    def __init__(self, count: int) -> None:
        self._count = count

    def get_tasks(self) -> Iterable[Task]:
        for i in range(self._count):
            yield Task(id=i, payload={"generated": True})