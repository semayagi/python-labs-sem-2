from typing import List, Iterable

from src.contracts.task_source import TaskSource
from src.models.task import Task

class TaskReceiver:
    '''
    Service for receiving tasks from different sources
    '''

    def receive(self, source: TaskSource) -> List[Task]:
        ''' Method that receives tasks from a source '''
        if not isinstance(source, TaskSource): # Runtime contract check
            raise TypeError("Source does not implement TaskSource protocol")
        
        return list(source.get_tasks())
    
    def receive_many(self, sources: Iterable[TaskSource]) -> List[Task]:
        ''' Method that receives tasks from several sources simultaneously '''
        tasks: List[Task] = []

        for source in sources:
            tasks.extend(self.receive(source))

        return tasks

