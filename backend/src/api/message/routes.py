from fastapi import APIRouter
from starlette.websockets import WebSocket, WebSocketDisconnect

from api.message.schemas import CreateMessage, MessageDTO
from api.message.service import MessageService
from core.websocket.manager import WebSocketManager

router = APIRouter(
    prefix="/messages",
)

websocket_manager = WebSocketManager()


@router.get("/", response_model=list[MessageDTO])
async def get_all_messages():
    return await MessageService.get_all_messages()


@router.get("/count")
async def get_messages_count():
    return await MessageService.get_messages_count()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket_manager.connect(websocket)
    try:
        while True:
            message_data = CreateMessage(text=await websocket.receive_text())
            message = await MessageService.add_message(text=message_data.text)
            await websocket_manager.broadcast(MessageDTO.model_validate(message, from_attributes=True))
    except WebSocketDisconnect:
        websocket_manager.disconnect(websocket)
