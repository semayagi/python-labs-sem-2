from typing import Iterable

from src.models.task import Task


class FileTaskSource:
    """
    Загружает задачи из файла построчно
    Формат: {id},{payload}
    """

    def __init__(self, filepath: str) -> None:
        self._filepath = filepath

    def get_tasks(self) -> Iterable[Task]:
        with open(self._filepath, "r", encoding="utf-8") as file:
            for line in file:
                task_id, payload = line.strip().split(',')
                yield Task(id=int(task_id), payload=payload)