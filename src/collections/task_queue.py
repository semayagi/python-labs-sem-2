from src.collections.iterators.task_iterator import TaskIterator
from src.collections.iterators.task_filterable_iterator import TaskFilterableIterator
from src.contracts.task_source import TaskSource
from src.models.task import Status

class TaskQueue:
    def __init__(self, task_sources: list[TaskSource] | None = []):
        self.__sources: list[TaskSource] = task_sources if task_sources else []
        self.__status_filter = None
        self.__priority_filter = None
        
    def __iter__(self):
        if self.__status_filter or self.__priority_filter:
            return TaskFilterableIterator(self.__sources, self.__status_filter, self.__priority_filter)
        return TaskIterator(self.__sources)
    
    def add(self, task_source: TaskSource):
        self.__sources.append(task_source)

    def reset_filtration(self):
        self.__status_filter = None
        self.__priority_filter = None

    def set_filtration(self, status_filter: Status | None, priority_filter: int | None):
        self.__status_filter = status_filter
        self.__priority_filter = priority_filter
        

        
        