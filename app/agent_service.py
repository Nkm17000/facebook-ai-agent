from app.config import Config
from app.messages import messages
from app.logger import logger
from app.groq_client import client
from app.facebook_service import FacebookService


class AgentService:

    @staticmethod
    def generate_post() -> str:
        """
        Generate lesson content using the Groq LLM.
        """

        logger.info("Generating lesson using model: %s", Config.MODEL)

        try:
            response = client.chat.completions.create(
                model=Config.MODEL,
                messages=messages,
                temperature=0.8
            )

            lesson = response.choices[0].message.content

            logger.info(
                "Lesson generated successfully. Length=%d",
                len(lesson)
            )

            return lesson

        except Exception:
            logger.exception("Failed to generate lesson")
            raise

    @staticmethod
    def publish() -> dict:
        """
        Generate lesson and publish it to Facebook.
        """

        logger.info("Facebook publishing started")

        try:
            lesson = AgentService.generate_post()

            logger.info("Posting lesson to Facebook")

            response = FacebookService.post_to_facebook(
                message=lesson
            )

            logger.info("Facebook post completed successfully")

            return response

        except Exception:
            logger.exception("Publishing failed")
            raise