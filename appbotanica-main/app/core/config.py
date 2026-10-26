import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FloraCheck API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "default_secret"
    DATABASE_URL: str = "sqlite:///./floracheck.db"

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()