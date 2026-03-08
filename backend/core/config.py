# backend/core/config.py

from pydantic_settings import BaseSettings

# BaseSettings automatically reads from your .env file
# This means you never hardcode secrets in your code
class Settings(BaseSettings):
    anthropic_api_key: str        # Required — will crash loudly if missing
    app_env: str = "development"  # Optional — has a default value

    class Config:
        env_file = ".env"         # Tells pydantic where to find the .env file

# We create one instance and import it everywhere
# This is called the "singleton pattern" — one shared config object
settings = Settings()