import asyncio
from src.models.task import Task
from src.infrastructure.logger import logger

class FileSaveHandler:
    '''Handler saves task info to file'''
    def __init__(self, filename: str = "processed_tasks.txt"):
        self.filename = filename

    async def handle(self, task: Task) -> None:
        await asyncio.to_thread(self._save_to_file, task)
        logger.info(f"[FileSaveHandler] Task {task.id} has been successfully saved to file.")

    def _save_to_file(self, task: Task) -> None:
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(f"ID: {task.id} | Description: {task.description} | Status: {task.status.value}\n")