from fastapi import FastAPI, HTTPException

from app.agent_service import AgentService
from app.config import Config
from app.logger import logger

# Validate configuration at startup
Config.validate()

app = FastAPI(
    title="Facebook Agent",
    version="1.0.0"
)


@app.get("/")
def home():
    logger.info("Home API called")

    return {
        "message": "Welcome to Facebook Agent",
        "status": "UP",
        "version": app.version
    }


@app.get("/agent")
def run_agent():
    logger.info("Agent execution started")

    try:
        response = AgentService.publish()

        logger.info("Agent execution completed successfully")

        return {
            "status": "SUCCESS",
            "response": response
        }

    except Exception as ex:
        logger.exception("Agent execution failed")

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )


@app.get("/health")
def health():
    logger.info("Health API called")

    return {
        "status": "UP"
    }