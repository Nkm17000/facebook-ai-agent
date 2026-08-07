from fastapi import FastAPI
from app.agent import say_hello
import logging
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

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
    facebook_page_id = os.getenv("FACEBOOK_PAGE_ID")
    logger.info(f"id : {facebook_page_id}")
    logger.info(f"Last 4 chars: {facebook_page_id[-4:]}")
    return {
        "message": "Hello World!" + facebook_page_id
    }


@app.get("/agent")
def agent():
    return say_hello()


@app.get("/health")
def health():
    return {
        "status": "UP"
    }