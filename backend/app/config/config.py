

from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

ENV_PATH = Path(__file__).resolve().parent.parent / ".env"


class DatabaseSettings(BaseSettings):
    DATABASE_URL: str


class AuthSettings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str =  "HS256"
    ACCESS_TOKEN_EXPIRE_HOURS: int = 12


class Settings(DatabaseSettings, AuthSettings):
    model_config = SettingsConfigDict(
        env_file=ENV_PATH,
        extra="ignore"
    )


settings = Settings()

