import openai
from config import settings

class OpenAIClient:
    """Cliente responsável por fazer chamadas para a API da OpenAI."""

    def __init__(self):
        self.api_key = settings.OPENAI_API_KEY

    def chat_completion(self, messages: list[dict]) -> str:
        """Envia mensagens para a API da OpenAI e retorna a resposta."""
        response = openai.ChatCompletion.create(
            model=settings.OPENAI_MODEL,
            messages=messages,
            api_key=self.api_key
        )
        return response["choices"][0]["message"]["content"]

openai_client = OpenAIClient()
