from groq import Groq
from app.config import Config

client = Groq(
    api_key=Config.GROQ_API_KEY
)