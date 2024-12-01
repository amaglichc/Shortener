from datetime import datetime, timezone, timedelta
from uuid import uuid4
from DB.core import session_maker
from DB.ORMs.UrlOrm import ShortenedURLOrm
from Schemas.URLShemas import ShortenedURLSchema
from config import config
from utils import generate_short_url


async def create_url(url: str):
    async with session_maker.begin() as session:
        now: datetime = datetime.now(timezone.utc)
        exp: datetime = now + timedelta(hours=24)
        orm: ShortenedURLOrm = ShortenedURLOrm(
            id=str(uuid4()),
            url=url,
            shortened_url=f"https://{config.DOMAIN}/{generate_short_url()}",
            created_at=now,
            expires_at=exp,
        )
        session.add(orm)
        session.commit()
        return ShortenedURLSchema.model_validate(orm, from_attributes=True)
