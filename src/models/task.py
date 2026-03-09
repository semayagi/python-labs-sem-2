from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)  # slots=True экономит память, т.к. вместо того, чтобы в каждом экземпляре определять свой __dict__ мы определяем один общий, неизменяемый набор аттрибутов __slots__
class Task:
    """
    Модель задачи
    """

    id: int
    payload: Any