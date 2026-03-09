from typing import Protocol, Iterable, runtime_checkable
from src.models.task import Task


@runtime_checkable  # для возможности проверки isinstance(obj, TaskSource)
class TaskSource(Protocol):
    """
    Контракт источника задач
    Любой объект с методом get_tasks считается источником
    """

    def get_tasks(self) -> Iterable[Task]:
        ...