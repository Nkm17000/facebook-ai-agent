from fastapi import FastAPI
from app.agent import say_hello

app = FastAPI(
    title="Facebook Agent",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "Hello World!"
    }


@app.get("/agent")
def agent():
    return say_hello()


@app.get("/health")
def health():
    return {
        "status": "UP"
    }