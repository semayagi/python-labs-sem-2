from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)  # slots=True экономит память, т.к. вместо того, чтобы в каждом экземпляре определять свой __dict__ мы определяем один общий, неизменяемый набор аттрибутов __slots__
class Task:
    """
    Модель задачи
    """

    def __init__(self, id: int, payload: Any):
        self.__id = id
        
        
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value: int):
        if not isinstance(value, int):
            raise TypeError("...")
        self.__id = value
    
    @id.deletter
	def name(self):
		print("Deleting name...")
		del self.__id
