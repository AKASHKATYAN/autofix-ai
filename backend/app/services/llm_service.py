from groq import Groq

from app.core.config import settings
from app.logging import logger


class LLMService:

    def __init__(self):

        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

        logger.info(
            "Groq client initialized."
        )

    def generate_response(
        self,
        prompt: str
    ):

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content