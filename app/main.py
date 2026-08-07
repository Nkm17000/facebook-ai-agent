from fastapi import FastAPI
from app.agent import say_hello
import logging


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Facebook Agent",
    version="1.0"
)


@app.get("/")
def home():
    logger.info("Home API called")
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