from datetime import datetime

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
