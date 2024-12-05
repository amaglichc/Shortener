from pydantic_settings import BaseSettings


class Config(BaseSettings):
    DB_URL: str
    DOMAIN: str


config = Config()
print(config.DB_URL)
