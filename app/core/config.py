import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Book Management GenAI"
    POSTGRES_URL: str = os.getenv("POSTGRES_URL", "postgresql+asyncpg://user:pass@localhost/bookdb")
    LLAMA_ENDPOINT: str = os.getenv("LLAMA_ENDPOINT", "http://localhost:11434/generate")
    
settings = Settings()