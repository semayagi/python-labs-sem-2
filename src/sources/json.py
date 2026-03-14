import json
from typing import Iterable

from src.models.task import Task

class JSONTaskSource:
    '''
    Reads and parses tasks from a given JSON file
    Format:
    {
        "tasks": [
            { "id1": int, "payload1": obj },
                        ...,
            { "id_n": int, "payload_n": obj }
        ]
    }
    '''

    def __init__(self, filepath: str) -> None:
        self._filepath = filepath

    def get_tasks(self) -> Iterable[Task]:
        ''' Method that implements reading and parsing '''
        with open(self._filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
            for task in data["tasks"]:
                yield Task(id=task["id"], payload=task["payload"])
                