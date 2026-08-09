from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./fluento.db" 
    SECRET_KEY: str = "thisisaverysecretkey"
    ALGORITHM: str = "HS256"

settings = Settings()
