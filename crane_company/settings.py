from pydantic_settings import BaseSettings
from pydantic import PostgresDsn, Field, SecretStr


class AppSettings(BaseSettings):
    company_db_uri: PostgresDsn = Field(
        default=...,
    )
    auth_jwt_secret: SecretStr = Field(default=...)
    auth_jwt_encoding_algorithm: str = Field(default=...)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"
        env_prefix = "crane_"


settings = AppSettings()
