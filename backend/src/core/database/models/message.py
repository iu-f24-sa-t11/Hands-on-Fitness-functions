from datetime import datetime

from beanie import Document


class Message(Document):
    text: str
    created_at: datetime

    class Settings:
        collection = "messages"
        indexes = ["created_at"]
