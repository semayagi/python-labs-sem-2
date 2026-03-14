from typing import Iterable

from src.models.task import Task

class APITaskSource:
    '''
    External API mock
    '''

    def get_tasks(self) -> Iterable[Task]:
        return [
            Task(id=100, payload={"api": "data1"}),
            Task(id=101, payload={"api": "data2"}),
        ]