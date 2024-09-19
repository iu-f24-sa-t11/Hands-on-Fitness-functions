from datetime import datetime

from fastapi import HTTPException

from config import DELETE_CODE
from core.database.models.message import Message


class MessageService:
    @staticmethod
    async def add_message(text: str) -> Message:
        message = Message(text=text, created_at=datetime.now())
        await message.insert()

        return message

    @staticmethod
    async def get_all_messages() -> list[Message]:
        messages = await Message.all().to_list()
        return messages

    @staticmethod
    async def get_messages_count() -> int:
        count = await Message.count()
        return count

    @staticmethod
    async def delete_all_messages(delete_code: str):
        if DELETE_CODE is None:
            raise HTTPException(status_code=400, detail="Deletion is not allowed.")
        if delete_code != DELETE_CODE:
            raise HTTPException(status_code=400, detail="Invalid delete code.")
        await Message.delete_all()
