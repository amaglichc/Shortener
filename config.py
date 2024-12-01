from os import getenv
from pydantic import BaseModel
from dotenv import load_dotenv


load_dotenv()


class Config(BaseModel):
    DB_URL: str = getenv("DB_URL")
    DOMAIN: str = getenv("DOMAIN")


config = Config()
