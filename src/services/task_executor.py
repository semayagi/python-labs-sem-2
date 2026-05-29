import asyncio
from src.models.task import Task
from src.contracts.async_task_handler import TaskHandler
from src.infrastructure.logger import logger

class TaskExecutor:
    def __init__(self):
        self._queue: asyncio.Queue[Task] = asyncio.Queue()

        self._handlers: dict[str, TaskHandler] = {} # { "task_type": handler }
        self._workers = []

    def register_handler(self, task_type: str, handler: TaskHandler) -> None:
        '''Registration of handlers for different types of tasks'''
        self._handlers[task_type] = handler

    async def add_task(self, task: Task) -> None:
        '''Method adds tasks in asyncronous queue.'''
        await self._queue.put(task)
        logger.info(f"[Executor] Task {task.id} was put to asyncronous queue.")

    async def start_workers(self, count: int) -> None:
        '''Launches background workers'''
        for i in range(count):
            worker = asyncio.create_task(self._worker_loop(i))
            self._workers.append(worker)
        logger.info(f"[Executor] Count of launched workers: {count}")

    async def _worker_loop(self, worker_id: int) -> None:
        '''Infinite worker loop for task handling'''
        while True:
            task = await self._queue.get()
            try:
                task_type = "io" if "save" in task.description.lower() else "network"
                
                handler = self._handlers.get(task_type)
                if handler:
                    await handler.handle(task)
                else:
                    logger.warning(f"[Worker {worker_id}] Handler of '{task_type}' type was not found.")
            except Exception as e:
                logger.error(f"[Worker {worker_id}] Error while handling task with id={task.id}: {e}")
            finally:
                self._queue.task_done()

    async def stop(self):
        '''Called to cancel background tasks when program finishes'''
        for worker in self._workers:
            worker.cancel()
        await asyncio.gather(*self._workers, return_exceptions=True)