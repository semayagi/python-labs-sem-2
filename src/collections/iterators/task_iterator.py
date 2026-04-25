from src.contracts.task_source import TaskSource
class TaskIterator:
    def __init__(self, task_sources: list[TaskSource]):
        self.__sources = iter(task_sources)
        # I am not sure, but the following line should return the iterator and shouldn't calculate the whole get_tasks() list beforehand (lazy loading):
        self.__source = iter(next(self.__sources).get_tasks())
        
    def __iter__(self):
        return self
        
    def __next__(self): 
        try:
            return next(self.__source)
        except StopIteration:
            next_source = next(self.__sources).get_tasks()
            try:
                self.__source = iter(next_source)
                return next(self.__source)
            except:
                raise StopIteration
            

		