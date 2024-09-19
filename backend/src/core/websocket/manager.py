from typing import List

from fastapi import WebSocket
from pydantic import BaseModel


class WebSocketManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.messages: List[str] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    @staticmethod
    async def send_message(message: BaseModel, websocket: WebSocket):
        await websocket.send_json(message.model_dump_json(), mode="text")

    async def broadcast(self, message: BaseModel):
        for connection in self.active_connections:
            await self.send_message(message, connection)
