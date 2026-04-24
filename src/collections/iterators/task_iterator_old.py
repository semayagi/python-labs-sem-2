from src.models.task import Task

class TaskIterator:
    def __init__(self, start: int, end: int, tasks: list[Task]):
        self.__tasks = tasks
        self.__start = start
        self.__end = end
        self.__cur = start
        
    def __iter__(self):
        return self
        
    def __next__(self):        
        if (self.__cur == self.__end + 1):
            raise StopIteration
        index = min(self.__cur, self.__end)
        self.__cur += 1
        
        
        return self.__tasks[index]
		