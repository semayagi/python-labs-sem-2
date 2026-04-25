from src.collections.iterators.task_iterator import TaskIterator
from src.contracts.task_source import TaskSource
from src.models.task import Status

class TaskFilterableIterator:
    def __init__(self, task_sources: list[TaskSource], status_filter: Status | None, priority_filter: int | None):
        self.__sources = iter(task_sources)
        self.__source = iter(next(self.__sources).get_tasks())
        self.__status_filter = status_filter
        self.__priority_filter = priority_filter

    def __iter__(self):
        return self
        
    def __next__(self): 
        try:
            next_task = next(self.__source)
            # print(f"-----\nChecking task {next_task}...\nIts status: {next_task.status}\nIts priority: {next_task.priority}")
            status_match = (self.__status_filter == None) or (next_task.status == self.__status_filter)
            priority_match = (self.__priority_filter == None) or (next_task.priority == self.__priority_filter)
            # print(f"Status match: {status_match}\n Priority match: {priority_match}")
            if status_match and priority_match:
                # print(f"OK, Returning {next_task}\n-----")
                return next_task
            # print(f"No match. Returning next\n-----")
            return self.__next__()  # Can I?
        except StopIteration:
            try:
                self.__source = iter(next(self.__sources).get_tasks())
                # print("BUGAGAAAAAAAA!")
                return self.__next__()
            except:
                raise StopIteration
            

		