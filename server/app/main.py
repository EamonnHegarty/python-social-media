
from app.routers.post import router as post_router
from fastapi import FastAPI

# FROM root so you can see client & server
# uvicorn app.main:app --reload
# source venv/Scripts/activate

app = FastAPI()
app.include_router(post_router)


