import os
from dotenv import load_dotenv

# Override local env variables if .env changes
load_dotenv(override=True)


class Config:
    PAGE_ID = os.getenv("FACEBOOK_PAGE_ID")
    PAGE_TOKEN = os.getenv("FACEBOOK_PAGE_TOKEN")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    MODEL = "llama-3.3-70b-versatile"

    @staticmethod
    def validate():
        missing = []

        if not Config.PAGE_ID:
            missing.append("FACEBOOK_PAGE_ID")

        if not Config.PAGE_TOKEN:
            missing.append("FACEBOOK_PAGE_TOKEN")

        if not Config.GROQ_API_KEY:
            missing.append("GROQ_API_KEY")

        if missing:
            raise ValueError(
                f"Missing environment variables: {', '.join(missing)}"
            )