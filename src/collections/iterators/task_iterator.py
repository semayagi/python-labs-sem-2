from src.contracts.task_source import TaskSource
class TaskIterator:
    def __init__(self, task_sources: list[TaskSource]):
        self.__sources = iter(task_sources)
        self.__source = iter(next(self.__sources).get_tasks())
        self.__source_index = 0
        
    def __iter__(self):
        return self
        
    def __next__(self): 
        try:
            return next(self.__source)
        except StopIteration:
            # print("NOO!!! STOP!/")
            # for source in self.__sources:
            #     print("SOURCE:: ", source)
            try:
                self.__source = next(self.__sources)
                return next(self.__source)
            except:
                raise StopIteration
            
        # for source in self.__sources:
        #     for task in source.get_tasks():
        #         yield task

		