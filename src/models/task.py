from dataclasses import dataclass
from typing import Any

@dataclass(slots=True) # slots=True reduces memory usage because, instead of each class object having a __dict__ that allows defining new attributes, there is a single immutable set of attributes defined in __slots__
class Task:
    '''
    Task model
    '''

    id: int
    payload: Any

    # def __init__(self, id: int, payload: Any):
    #     self.__id = id
        
        
    # @property
    # def id(self):
    #     return self.__id
    
    # @id.setter
    # def id(self, value: int):
    #     if not isinstance(value, int):
    #         raise TypeError("...")
    #     self.__id = value
    
    # @id.deletter
	# def name(self):
	# 	print("Deleting name...")
	# 	del self.__id
