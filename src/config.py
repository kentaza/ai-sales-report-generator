import os
from dataclasses import dataclass


@dataclass
class Settings:
    app_name: str
    app_env: str
    app_host: str
    app_port: int
    log_level: str
    openai_api_key: str


settings = Settings(
    app_name=os.getenv("APP_NAME", "AI Sales Report Generator"),
    app_env=os.getenv("APP_ENV", "development"),
    app_host=os.getenv("APP_HOST", "0.0.0.0"),
    app_port=int(os.getenv("APP_PORT", "8000")),
    log_level=os.getenv("LOG_LEVEL", "INFO"),
    openai_api_key=os.getenv("OPENAI_API_KEY", ""),
)
