from beanie import init_beanie
from motor import motor_asyncio

from config import DB_HOST, DB_NAME
from core.database.models.message import Message

ALL_MODELS = [
    Message
]


async def init_db():
    client = motor_asyncio.AsyncIOMotorClient(DB_HOST)
    database = client[DB_NAME]
    await init_beanie(database=database, document_models=ALL_MODELS)
