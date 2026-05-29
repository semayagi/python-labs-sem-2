import asyncio
import datetime
import pytest
from src.models.task import Task, Status
from src.services.task_executor import TaskExecutor

def make_test_task(task_id: str, description: str = "Test task") -> Task:
    return Task(
        id=task_id,
        description=description,
        priority=1,
        deadline=datetime.date.today(),
        status=Status.pending
    )

class DummyHandler:
    def __init__(self):
        self.processed_tasks = []
        self.is_opened = False

    async def __aenter__(self):
        self.is_opened = True
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.is_opened = False

    async def handle(self, task: Task) -> None:
        self.processed_tasks.append(task)
        task.status = Status.done


@pytest.mark.asyncio
async def test_executor_processes_task_successfully():
    executor = TaskExecutor()
    
    io_handler = DummyHandler()
    network_handler = DummyHandler()
    
    executor.register_handler("io", io_handler)
    executor.register_handler("network", network_handler)
    
    task = make_test_task("1", description="save results to file")

    await executor.add_task(task)
    
    await executor.start_workers(count=1)
    
    await asyncio.wait_for(executor._queue.join(), timeout=1.0)
    
    await executor.stop()

    assert len(io_handler.processed_tasks) == 1
    assert io_handler.processed_tasks[0].id == "1"
    assert task.status == Status.done
    assert len(network_handler.processed_tasks) == 0


@pytest.mark.asyncio
async def test_executor_handles_unknown_task_type_safely():
    executor = TaskExecutor()
    
    task = make_test_task("2", description="unknown operation")

    await executor.add_task(task)
    
    await executor.start_workers(count=1)
    
    await asyncio.wait_for(executor._queue.join(), timeout=1.0)
    
    await executor.stop()

    assert task.status == Status.pending


@pytest.mark.asyncio
async def test_socket_handler_context_manager():
    from src.handlers.socket_reader import SocketReaderHandler
    
    async with SocketReaderHandler(host="127.0.0.1", port=8888) as handler:
        assert handler.server is not None
        assert handler.server.is_serving() 
    
    assert handler.server is None or not handler.server.is_serving()