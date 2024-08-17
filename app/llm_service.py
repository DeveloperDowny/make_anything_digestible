from openai import OpenAI
import logging
from config.config import Config

from dummy_data import dumm_htmlContent

logger = logging.getLogger(__name__)


class LLMService:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def dummy_generate_response(self, topic: str) -> str:
        return dumm_htmlContent

    def generate_response(self, topic: str) -> str:
        """Generate a response using OpenAI's gpt-4o-mini model."""

        if Config.DEBUG:
            return self.dummy_generate_response(topic)

        prompt = Config.MPROMPT + " <topic> " + topic + "</topic>"
        try:

            messagePayload = {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                ],
            }
            logger.info(f"Generating explanation for image: {topic}")

            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[messagePayload],
                max_tokens=800,
            )

            explanation = response.choices[0].message.content
            logger.info(f"Generated explanation: {explanation}")
            return explanation
        except Exception as e:
            error_msg = f"Error generating response: {str(e)}"
            logger.error(error_msg)
            raise Exception(error_msg)
