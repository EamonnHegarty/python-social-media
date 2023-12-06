from app.routers.post import router as post_router
from fastapi import FastAPI

# FROM /server
# uvicorn app.main:app --reload
# source .venv/Scripts/activate

app = FastAPI()
app.include_router(post_router)
