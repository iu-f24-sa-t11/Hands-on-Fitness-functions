from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.message.routes import router as messages_router
from config import APP_ROOT_PATH
from core.database.db import init_db
# import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()

    yield


app = FastAPI(
    root_path=APP_ROOT_PATH,
    lifespan=lifespan
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(messages_router)


@app.get("/")
async def get_hello_world():
    return {"message": "Hello, world!"}
