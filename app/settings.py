import os
from typing import Optional
from pydantic_settings import BaseSettings

# Specify where the enviroment file is
DOTENV = os.path.join(os.path.dirname(__file__), ".env")


class Settings(BaseSettings):
    sendgrid_api_key: Optional[str] = None
    database_url: Optional[str] = None
    twilio_account_sid: Optional[str] = None
    twilio_auth_token: Optional[str] = None

    class Config:
        env_file = DOTENV


# Create an instance of Settings to be accessed
settings = Settings()
