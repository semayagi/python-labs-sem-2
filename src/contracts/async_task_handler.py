from typing import Protocol, runtime_checkable
from src.models.task import Task


@runtime_checkable
class TaskHandler(Protocol):
    '''
    Async Task Handler protocol
    Any object with a handle method is considered a handler
    '''

    async def handle(self, task: Task) -> None:
        ...
        
