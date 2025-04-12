"""
Loads environment variables and application settings.
"""
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:#pylint: disable=too-few-public-methods
    """Holds configuration for project-wide settings."""
    PROJECT_NAME: str = "Book Management GenAI"
    POSTGRES_URL: str = os.getenv("POSTGRES_URL", "postgresql+asyncpg://user:pass@localhost/bookdb")
    LLAMA_ENDPOINT: str = os.getenv("LLAMA_ENDPOINT", "http://localhost:11434/generate")

settings = Settings()
