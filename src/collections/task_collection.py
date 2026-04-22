from src.collections.iterators.task_iterator import TaskIterator
from src.models.task import Task

# FIFO - First in, first out 1-2-3 -> 2-3 -> 3
class TaskQueue:
    def __init__(self, tasks: list[Task], start: int, end: int):
        self.__tasks = tasks
        self.__start = start
        self.__end = end

    def __iter__(self):
        return TaskIterator(start=self.__start, end=self.__end)