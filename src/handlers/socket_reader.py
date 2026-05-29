import asyncio
from src.models.task import Task
from src.infrastructure.logger import logger

class SocketReaderHandler:
    '''
    Socket handler, which works like server.
    Handles resources with asyncronous context manager.
    '''
    def __init__(self, host: str = "127.0.0.1", port: int = 1025):
        self.host = host
        self.port = port
        self.server = None

    async def __aenter__(self):
        # async TCP-server
        self.server = await asyncio.start_server(self._handle_client, self.host, self.port)
        logger.info(f"[SocketHandler] Server is running at {self.host}:{self.port}")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.server:
            self.server.close()
            await self.server.wait_closed()
            logger.info("[SocketHandler] Server is stopped, ports are freed.")

    async def _handle_client(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        '''OS pings this method during client connection through terminal'''
        data = await reader.read(100)
        message = data.decode().strip()
        addr = writer.get_extra_info('peername')
        
        logger.info(f"[SocketHandler] Received data from {addr}: '{message}'")
        
        # echo to client
        writer.write(f"Echo: {message}\n".encode())
        await writer.drain()
        writer.close()
        await writer.wait_closed()

    async def handle(self, task: Task) -> None:
        logger.info(f"[SocketHandler] Network analysis started for task {task.id}...")
        await asyncio.sleep(1.5) 
        logger.info(f"[SocketHandler] Analysis of task {task.id} finished.")