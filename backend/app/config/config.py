

from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class DatabaseSettings(BaseSettings):
    DATABASE_URL: str


class AuthSettings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str =  "HS256"
    ACCESS_TOKEN_EXPIRE_HOURS: int = 12


class Settings(DatabaseSettings, AuthSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


@lru_cache
def get_settigs():
    return Settings()


settings = get_settigs()

