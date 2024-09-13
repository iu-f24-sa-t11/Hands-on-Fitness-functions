from fastapi import FastAPI

from src.config import APP_ROOT_PATH

app = FastAPI(
    root_path=APP_ROOT_PATH
)


@app.get("/")
async def get_hello_world():
    return {"message": "Hello, world!"}
