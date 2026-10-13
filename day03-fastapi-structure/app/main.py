from fastapi import FastAPI

from app.routers import hello
from app.routers import user

app = FastAPI(
    title="Day 3 FastAPI Structure"
)

app.include_router(
    hello.router
)

app.include_router(
    user.router
)

@app.get("/")
def root():
    return {
        "message": "Day 3 FastAPI structure",
        "status": "running"
    }