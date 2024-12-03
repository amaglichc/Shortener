from datetime import datetime
from pydantic import BaseModel


class UrlToShortSchema(BaseModel):
    url: str


class ShortenedURLSchema(BaseModel):
    id: str
    url: str
    shortened_url: str
    user_id: str | None
    created_at: datetime
    expires_at: datetime
