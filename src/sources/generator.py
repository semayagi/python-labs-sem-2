from typing import Iterable
from src.models.task import Task
import datetime

class GeneratorTaskSource:
    '''
    Programmatically generates a specified number of tasks
    '''

    def __init__(self, count: int) -> None:
        self._count = count

    def get_task(self, index) -> Task:
        return Task(id=str(index),  
                       priority=1, 
                       deadline=datetime.date.fromisoformat(f"{2027+index}-01-01"), 
                       description=f"Generated task №{index}")

    def get_tasks(self) -> Iterable[Task]:
        ''' Method that implements task generating '''
        for i in range(self._count):
            yield self.get_task(i)