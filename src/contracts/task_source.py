from typing import Protocol, Iterable, runtime_checkable
from src.models.task import Task


@runtime_checkable  # To allow checking - isinstance(obj, TaskSource)
class TaskSource(Protocol):
    '''
    Task Source protocol
    Any object with a get_tasks method is considered a source
    '''

    def get_tasks(self) -> Iterable[Task]:
        ...