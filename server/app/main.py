from contextlib import asynccontextmanager

from app.database import database
from app.routers.post import router as post_router
from app.routers.user import router as user_router
from fastapi import FastAPI

# FROM /server
# uvicorn app.main:app --reload
# source .venv/Scripts/activate


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)


app.include_router(post_router)
app.include_router(user_router)
