from src.models.descriptors.basic_field import BasicField
from src.infrastructure.logger import logger

class UndeletableField(BasicField):
    ''' Undeletable field descriptor for task model '''
    def __init__(self, expected_type: type, nullable: bool = False):
        self.expected_type = expected_type
        self.nullable = nullable

    def __delete__(self, obj):
        logger.error(f"{self.attr_name} field of Task object cannot be deleted.")
        raise PermissionError(f"{self.attr_name} field of Task object cannot be deleted.")