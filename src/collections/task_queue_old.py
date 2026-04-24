from src.collections.iterators.task_iterator import TaskIterator
from src.models.task import Task

class TaskQueue:
    def __init__(self, tasks: list[Task] = []):
        self.__tasks = tasks
        self.__start = 0
        self.__end = len(tasks) - 1
        
    def __getitem__(self, index: int):
        return self.__tasks[index]
        
    def __len__(self):
        return len(self.__tasks)

    def __iter__(self):
        return TaskIterator(start=self.__start, end=self.__end, tasks=self.__tasks)

    def __setitem__(self, index: int, task: Task):
        if not isinstance(task, Task):
            return NotImplemented
        self.__tasks[index] = task
        
        