from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str = "AutoFix-AI"

    APP_VERSION: str = "1.0.0"

    DEBUG: bool = True

    DATABASE_URL: str

    GITHUB_TOKEN: str = ""

    GROQ_API_KEY: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()