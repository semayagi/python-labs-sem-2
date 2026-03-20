from dataclasses import dataclass
from typing import Protocol, Any
import datetime

@dataclass(slots=True) # slots=True reduces memory usage because, instead of each class object having a __dict__ that allows defining new attributes, there is a single immutable set of attributes defined in __slots__
class Task(Protocol):
    '''
    Task model
    '''

    id: str
    payload: dict[str, Any]
    
    def execute(self, *args, **kwargs) -> Any:
        ...
        
    @property
    def task_type(self):
        ...
        
    @property
    def deadline(self) -> datetime.date | None:
        ...
    
    
class FileTask(Task):
    id: str
    payload: dict[str, Any]
    
    @property
    def deadline(self):
        return self.payload["deadline"]
    
    