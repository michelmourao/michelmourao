import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "IA Chat API"
    HOST: str = "127.0.0.1"
    PORT: int = 8000
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL: str = "gpt-4"

settings = Settings()
