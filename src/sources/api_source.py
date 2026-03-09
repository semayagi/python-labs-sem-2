from typing import Iterable

from src.models.task import Task

class ApiTaskSource:
    """
    Заглушка внешнего API 
    """

    def get_tasks(self) -> Iterable[Task]:
        return [
            Task(id=100, payload={"api": "data1"}),
            Task(id=101, payload={"api": "data2"}),
        ]