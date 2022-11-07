import os

from pydantic import AnyUrl, BaseSettings, Field, PostgresDsn


class AppSettings(BaseSettings):
    class Config:
        case_sensitive = True

    # loaded from environment vars
    ENVIRONMENT: str = os.environ["ENVIRONMENT"]

    POSTGRES_USER: str = os.environ["POSTGRES_USER"]
    POSTGRES_PASSWORD: str = os.environ["POSTGRES_PASSWORD"]
    DATABASE_PORT: int = os.environ["DATABASE_PORT"]
    DATABASE_HOST: str = os.environ["DATABASE_HOST"]
    DATABASE_NAME: str = os.environ["DATABASE_NAME"]

    ALLOWED_CORS_ORIGINS: set[AnyUrl] = os.environ["ALLOWED_CORS_ORIGINS"]

    # dynamically generated
    POSTGRES_DSN: PostgresDsn = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"


settings = AppSettings()
