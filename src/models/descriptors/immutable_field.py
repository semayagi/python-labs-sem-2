from src.models.descriptors.undeletable_field import UndeletableField
from src.infrastructure.logger import logger

class ImmutableField(UndeletableField):
    ''' Immutable field descriptor for task model '''
    def __set__(self, obj: "Task", value):
        if self.attr_name in vars(obj):
            logger.error(f"{self.attr_name} field of {obj.__name__} object of Task class is set only once and cannot be modified.")
            raise PermissionError(f"{self.attr_name} field of {obj.__name__} object of Task class is immutable.")
        super().__set__(obj, value)
