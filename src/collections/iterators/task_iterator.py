# from src.contracts.task_source import TaskSource
# class TaskIterator:
#     def __init__(self, task_sources: list[TaskSource]):
#         self.__tasks = []
#         for source in task_sources:
#             self.__tasks.extend(source.get_tasks())
#         self.__index = 0
        
#     def __iter__(self):
#         return self
        
#     def __next__(self): 
#         if self.__index >= len(self.__tasks):
#             raise StopIteration
#         task = self.__tasks[self.__index]
#         self.__index += 1
#         return task

		