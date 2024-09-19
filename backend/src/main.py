import os
from contextlib import asynccontextmanager
from fastapi.exceptions import HTTPException

from fastapi import FastAPI

from api.message.routes import router as messages_router
from config import APP_ROOT_PATH, DROP_CODE
from core.database.db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()

    yield


app = FastAPI(
    root_path=APP_ROOT_PATH,
    lifespan=lifespan
)

app.include_router(messages_router)


@app.post("/drop-application")
async def drop_application(drop_code: str):
    if DROP_CODE is None:
        raise HTTPException(status_code=400, detail="Dropping is not allowed.")
    if drop_code != DROP_CODE:
        raise HTTPException(status_code=400, detail="Invalid drop code.")
    os._exit(1)
