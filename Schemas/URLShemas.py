from datetime import datetime
from pydantic import BaseModel


class ShortenedURLSchema(BaseModel):
    id: str
    url: str
    shortened_url: str
    created_at: datetime
    expired_at: datetime
