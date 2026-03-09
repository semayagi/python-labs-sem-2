from typing import List, Iterable

from src.contracts.task_source import TaskSource
from src.models.task import Task

class TaskReceiver:
    """
    Сервис приёма задач из разных источников
    """

    def receive(self, source: TaskSource) -> List[Task]:
        # runtime-проверка контракта
        if not isinstance(source, TaskSource):
            raise TypeError("Source does not implement TaskSource protocol")
        
        return list(source.get_tasks())
    
    def receive_many(self, sources: Iterable[TaskSource]) -> List[Task]:
        """
        Приём задач сразу из нескольких источников
        """
        tasks: List[Task] = []

        for source in sources:
            tasks.extend(self.receive(source))

        return tasks

