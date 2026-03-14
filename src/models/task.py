from dataclasses import dataclass
from typing import Any

@dataclass(slots=True) # slots=True reduces memory usage because, instead of each class object having a __dict__ that allows defining new attributes, there is a single immutable set of attributes defined in __slots__
class Task:
    '''
    Task model
    '''

    id: int
    payload: Any