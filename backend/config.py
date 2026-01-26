from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    CORS_ORIGINS: str = "http://localhost:5173"
    DB_URL: str = "sqlite:///local.db"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
