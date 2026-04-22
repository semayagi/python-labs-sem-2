from src.models.task import Task

class TaskIterator:
    def __init__(self, tasks: list[Task], start: int, end: int):
        self.__tasks = tasks
        self.__start = start
        self.__end = end
        self.__cur = start
        
    def __iter__(self):
        return self
        
    def __next__(self):
        index = self.__cur
        self.__cur += 1
        return self.__tasks[self.__cur]
		