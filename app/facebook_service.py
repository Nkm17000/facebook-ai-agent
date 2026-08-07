import requests
from requests.exceptions import RequestException

from app.config import Config
from app.logger import logger


class FacebookService:
    BASE_URL = "https://graph.facebook.com/v23.0"

    @staticmethod
    def post_to_facebook(message: str) -> dict:
        logger.info("Starting Facebook post")
        logger.info("token", Config.PAGE_TOKEN[::])

        url = f"{FacebookService.BASE_URL}/{Config.PAGE_ID}/feed"

        payload = {
            "message": message,
            "access_token": Config.PAGE_TOKEN
        }

        try:
            response = requests.post(
                url,
                data=payload,
                timeout=30
            )

            logger.info("Facebook Response Code: %s", response.status_code)

            response.raise_for_status()

            result = response.json()

            logger.info("Facebook post created successfully")

            return result

        except RequestException as ex:
            logger.exception("Facebook API call failed")
            raise ex