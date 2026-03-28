from datetime import datetime, date
from src.models.descriptors.basic_field import BasicField
from src.models.descriptors.immutable_field import ImmutableField
from src.models.descriptors.undeletable_field import UndeletableField
from enum import Enum

class Status(Enum):
    pending = "pending"
    in_progress = "in_progress"
    done = "done"
    cancelled = "cancelled"


class Task:
    ''' Task model of the task processing platform '''
    
    id = ImmutableField(str)
    description = BasicField(str)
    priority = UndeletableField(int)
    status = UndeletableField(Status)
    created_at = UndeletableField(datetime)
    deadline = UndeletableField(date, nullable=True) 

    def __init__(self, id: str, description: str, priority: int, deadline: datetime | date, created_at: date | None = None, status: Status = Status.pending) -> None:
        self.id = id
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.created_at = created_at or datetime.now()
        self.status = status
        
    @property
    def is_ready(self) -> bool:
        """ True if status == pending """
        return self.status == Status.pending
    
    def __eq__(self, other: "Task"):
        if not isinstance(other, Task):
            return NotImplemented
        return self.id == other.id