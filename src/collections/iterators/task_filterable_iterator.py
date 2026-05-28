from src.collections.iterators.task_iterator import TaskIterator
from src.contracts.task_source import TaskSource
from src.models.task import Status

class TaskFilterableIterator:
    def __init__(self, task_sources: list[TaskSource], status_filter: Status | None, priority_filter: int | None):
        self.__tasks_gen = (
            task
            for source in task_sources
            for task in source.get_tasks()
            if (status_filter is None or task.status == status_filter)
            and (priority_filter is None or task.priority == priority_filter)
        )

    def __iter__(self):
        return self
        
    def __next__(self): 
        return next(self.__tasks_gen)
            

		