from __future__ import annotations
from src.infrastructure.logger import logger

class BasicField:
    ''' Basic descriptor for task model '''
    def __init__(self, expected_type: type, nullable: bool = False, deleted_value = ""):
        self.expected_type = expected_type
        self.nullable = nullable
        self.deleted_value = deleted_value

    def __set_name__(self, owner, name):
        self.attr_name = '_' + name

    def __get__(self, obj: "Task", cls: "type[Task]"):
        if obj is None:
            return self
        return getattr(obj, self.attr_name)
    
    def __set__(self, obj: "Task", value):
        if value is None:
            if self.nullable:
                setattr(obj, self.attr_name, value)
                return
            raise ValueError(f"Attribute '{self.attr_name.lstrip('_')}' cannot be None")

        if not isinstance(value, self.expected_type):
            logger.error(f"Expected {self.expected_type.__name__} type, got {value} of {type(value).__name__} type while setting {self.attr_name.lstrip('_')} attribute in {obj} object of Task class.")
            raise TypeError(f"Expected {self.expected_type.__name__}, got {type(value).__name__}")
        
        setattr(obj, self.attr_name, value)

    def __delete__(self, obj: "Task"):
        logger.info(f"Deleting {self.attr_name} field of {obj.__name__} object of Task class.")
        setattr(obj, self.attr_name, self.deleted_value)