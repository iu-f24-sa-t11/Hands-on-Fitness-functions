from fastapi import APIRouter
from starlette.responses import HTMLResponse
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

@router.get("/frontend")
async def get_frontend():
    html_content = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Chat</title>
        </head>
        <body>
            <h1>Chat</h1>
            <ul id="messages"></ul>
            <input id="message" type="text">
            <button onclick="sendMessage()">Send</button>
            <script>
                // get all messages
                fetch('/api/messages')
                    .then(response => response.json())
                    .then(messages => {
                        var messagesList = document.getElementById('messages');
                        messages.forEach(message => {
                            var messageElement = document.createElement('li');
                            var messageText = document.createTextNode(message.text);
                            messageElement.appendChild(messageText);
                            messagesList.appendChild(messageElement);
                        });
                    });
                
                var ws = new WebSocket("ws://localhost/api/messages/ws");
                ws.onmessage = function(event) {
                    var messagesList = document.getElementById('messages');
                    var messageElement = document.createElement('li');
                    var eventData = JSON.parse(event.data);
                    var eventData = JSON.parse(eventData);
                    console.log(eventData);
                    console.log(eventData.text);
                    var messageText = document.createTextNode(eventData.text);
                    messageElement.appendChild(messageText);
                    messagesList.appendChild(messageElement);
                };
                function sendMessage() {
                    var input = document.getElementById('message');
                    ws.send(input.value);
                    input.value = '';
                }
            </script>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
