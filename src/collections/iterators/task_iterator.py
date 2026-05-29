from src.contracts.task_source import TaskSource

# Fixed issues of 3rd Laboratory

class TaskIterator:
    def __init__(self, task_sources: list[TaskSource]):
        self.__tasks_gen = (
            task
            for source in task_sources
            for task in source.get_tasks()
        )
        
    def __iter__(self):
        return self
        
    def __next__(self): 
        return next(self.__tasks_gen)
            

		