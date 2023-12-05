from fastapi import FastAPI

# FROM root so you can see client & server
# uvicorn app.main:app --reload
# source venv/Scripts/activate

app = FastAPI()


@app.get("/")
async def root():
    print("hi")
    return {"message": "hello world"}
