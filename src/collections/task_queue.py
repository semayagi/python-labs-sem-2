# from src.collections.iterators.task_iterator import TaskIterator
# from src.models.task import Task
from src.contracts.task_source import TaskSource

class TaskQueue:
    def __init__(self, task_sources: list[TaskSource]):
        self.__sources = task_sources
        
    def __iter__(self):
        # return TaskIterator(task_sources=self.__sources)
        for source in self.__sources:
            for task in source.get_tasks():
                yield task

        
        