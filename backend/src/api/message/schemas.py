from datetime import datetime

from pydantic import BaseModel


class CreateMessage(BaseModel):
    text: str


class MessageDTO(BaseModel):
    text: str
    created_at: datetime
