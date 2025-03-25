from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    AUTH_SECRET_KEY: str
    AUTH_ALGORITHM: str
    API_URL: str
    URL_AZURE_IA: str
    ENDPOINT_KEY_IA_AZURE: str

    class Config:
        env_file = ".env"

settings = Settings()
