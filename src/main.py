import asyncio
from src.infrastructure.logger import logger
from src.models.task import Task
from src.services.task_executor import TaskExecutor
from src.handlers.file_save import FileSaveHandler
from src.handlers.socket_reader import SocketReaderHandler

async def main() -> None:
    logger.info("Asyncronous application is up.")

    # 1. Init handlers
    file_handler = FileSaveHandler("processed_tasks.txt")
    socket_handler = SocketReaderHandler(host="127.0.0.1", port=1025)

    # 2. Create task executor
    executor = TaskExecutor()
    executor.register_handler("io", file_handler)
    executor.register_handler("network", socket_handler)

    # 3. Enter socket server context, it begins listesting port
    async with socket_handler:
        
        # 4. Start workers pool (e.g., 3 parallel handlers)
        await executor.start_workers(count=3)

        # 5. Generate test tasks (imitation of sources)
        test_tasks = [
            Task(id="1", description="Save backup to disk", priority=5, deadline=None),
            Task(id="2", description="Network analysis data", priority=3, deadline=None),
            Task(id="3", description="Save user logs", priority=2, deadline=None),
            Task(id="4", description="Network ping status", priority=4, deadline=None),
        ]

        for task in test_tasks:
            await executor.add_task(task)

        print("\n SYSTEM IS READY. Switch terminal and execute: connect localhost 1025")
        print("Awaiting connections and finishing background tasks(30 seconds)...")
        await asyncio.sleep(30)

        await executor.stop()
        logger.info("Program finished.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nApplication was forced to stop by user.")