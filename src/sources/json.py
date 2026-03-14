import json
from typing import Iterable

from src.models.task import Task


class JSONTaskSource:
    """
    Парсит JSON
    Формат:
    {
        "id1": "payload1",
            ...,
        "id_n": "payload_n"
    }
    id: int
    payload: Object
    """

    def __init__(self, filepath: str) -> None:
        self._filepath = filepath

    def get_tasks(self) -> Iterable[Task]:
        with open(self._filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
            for task in data["tasks"]:
                yield Task(id=task["id"], payload=task["payload"])
                