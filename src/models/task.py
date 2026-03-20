from __future__ import annotations

import datetime
from typing import Any

from enum import Enum

class Status(Enum):
    pending = "pending"
    in_progress = "in_progress"
    done = "done"
    cancelled = "cancelled"

# data-descriptor
class TypedField:
    """
    Data descriptor - checks value type in __set__.

    Has priority above obj.__dict__['payload'] and non-data descriptors
    """

    def __init__(self, expected_type: type, nullable: bool = False) -> None:
        self._expected_type = expected_type
        self._nullable = nullable
        self._attr_name: str = ""

    def __set_name__(self, owner: type, name: str) -> None:
        # Python calls this method automatically when the class is created, for each field
        # We save the name under which the field is decalred in the class: _<name>
        # And store the actual value in it
        self._attr_name = f"_{name}"

    def __get__(self, obj: Any, objtype: type | None = None) -> Any:
        """
        Accesed via:
            - instance - return the attribute value
            - class - return the descriptor itself
              This follows the standard pattern that allows viewing
              Task.payload._expected_type and ._nullable settings
        """
        if obj is None:
            return self
        return getattr(obj, self._attr_name, None)

    def __set__(self, obj: Any, value: Any) -> None:
        if value is None:
            if self._nullable:
                setattr(obj, self._attr_name, value)
                return
            raise ValueError(
                f"Attribute '{self._attr_name.lstrip('_')}' cannot be None"
            )
        if not isinstance(value, self._expected_type):
            raise TypeError(
                f"Attribute '{self._attr_name.lstrip('_')}' must be "
                f"{self._expected_type.__name__}, got {type(value).__name__}"
            )
        setattr(obj, self._attr_name, value)

# non-data descriptor
class ReadOnlyField:
    """
    Raises AttributeError in case of attempt of updating the attribute with public API (obj.id = ...) 

    Can only be set in __init__ using self

    Differs from @property:
        - no __set__
        - therefore obj.__dict__["id"] = ... is allowed
        - on the other hand, even @property doesn't disallow obj.__dict__["_id"]
        - and actually this descriptor is created as an example of non-data descriptor (I would prefer to use @property for ID)
    """

    def __set_name__(self, owner: type, name: str) -> None:
        self._attr_name = f"_{name}"

    def __get__(self, obj: Any, objtype: type | None = None) -> Any:
        if obj is None:
            return self
        return getattr(obj, self._attr_name, None)



# ----------- Exceptions -----------

class TaskError(Exception):
    """Basic exception for task model"""


class InvalidStatusError(TaskError):
    """Invalid task status"""


class MissingPayloadKeyError(TaskError):
    """Accessing a non-existent key in the payload"""


# ----------- Task model -----------

class Task:
    """
    Task model of the task processing platform

    Attributes:
        id      - unique identifier (read-only, non-data descriptor)
        payload - arbitrary task data (data descriptor, only dict type)

    Calculated attributes (@property):
        status      - status + validation: pending/in_progress/done/cancelled
        created_at  - time of creation (read-only)
        deadline    - deadline from payload (or None)
        priority    - priority from payload (or None)
        is_ready    - returns True if the task is ready for execution 
    """

    payload: dict[str, Any] = TypedField(dict)
    id: str = ReadOnlyField()

    def __init__(self, id: str | int, payload: dict[str, Any]) -> None:
        self._id = str(id)
        self.payload = payload
        self._created_at = datetime.datetime.now()
        self._status: Status = Status.pending

    @property
    def created_at(self) -> datetime.datetime:
        """ Task creation time 
            Read-only           """
        return self._created_at

    @property
    def status(self) -> Status:
        """ Current task status """
        return self._status

    @status.setter
    def status(self, value: str) -> None:
        """ Sets the status checking if the value is allowed """
        if not isinstance(value, Status):
            raise InvalidStatusError(
                f"Invalid status '{value}'. "
                f"Expected a Status enum value (e.g. Status.pending)"
            )
        self._status = value

    @property
    def deadline(self) -> datetime.date | None:
        """ Deadline from payload['deadline'], or None if not specified """
        return self.payload.get("deadline")

    @property
    def priority(self) -> int | None:
        """ Priority from payload['priority'], or None if not specified """
        return self.payload.get("priority")

    @property
    def is_ready(self) -> bool:
        """ True if status == pending """
        return self._status == "pending"

    def __repr__(self) -> str:
        # !r adds quotes around str values, which adds unambiguity
        return (
            f"Task(id={self.id!r}, status={self.status!r}, "
            f"priority={self.priority!r}, deadline={self.deadline!r})"
        )