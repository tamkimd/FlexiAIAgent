from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    model_name: str = "gemma2:latest"
    serper_api_key: Optional[str] = None

    class Config:
        env_file = ".env"
