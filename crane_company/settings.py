from pydantic_settings import BaseSettings
from pydantic import PostgresDsn, Field


class AppSettings(BaseSettings):
    db_uri: PostgresDsn = Field(default=...)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"
        env_prefix = "crane_company_"


settings = AppSettings()
