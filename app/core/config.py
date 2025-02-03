from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "Number Classification API"
    API_VERSION: str = "1.0.0"
    ALLOWED_ORIGINS: List[str] = ["*"]  # In production, replace with specific origins
    NUMBERS_API_BASE_URL: str = "http://numbersapi.com"

    class Config:
        case_sensitive = True

settings = Settings()