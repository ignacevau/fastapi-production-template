from pydantic import AnyUrl, BaseSettings, PostgresDsn


class AppSettings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    DATABASE_URL: PostgresDsn
    ALLOWED_CORS_ORIGINS: set[AnyUrl]
    ENVIRONMENT: str = "development"


settings = AppSettings()
