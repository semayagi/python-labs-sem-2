from typing import Iterable
from src.models.task import Task
import datetime

class GeneratorTaskSource:
    '''
    Programmatically generates a specified number of tasks
    '''

    def __init__(self, count: int) -> None:
        self._count = count

    def get_tasks(self) -> Iterable[Task]:
        ''' Method that implements task generating '''
        for i in range(self._count):
            yield Task(id=i, payload={
                                "priority": 1,
                                "deadline": datetime.date.fromisoformat(f"{2000+i}-01-01"),
                                "description": f"Generated task №{i}"
                            })