from datetime import datetime, timezone, timedelta
from uuid import uuid4
from DB.core import session_maker
from DB.ORMs.UrlOrm import ShortenedURLOrm
from Schemas.URLShemas import ShortenedURLSchema
from sqlalchemy import select
from fastapi import HTTPException,status
from utils import generate_short_url


async def create_url(url: str):
    async with session_maker.begin() as session:
        now: datetime = datetime.now(timezone.utc)
        exp: datetime = now + timedelta(hours=24)
        orm: ShortenedURLOrm = ShortenedURLOrm(
            id=str(uuid4()),
            url=url,
            shortened_url=generate_short_url(),
            created_at=now,
            expires_at=exp,
        )
        session.add(orm)
        session.commit()
        return ShortenedURLSchema.model_validate(orm, from_attributes=True)


async def get_url(shorted_url: str):
    async with session_maker.begin() as session:
        orm: ShortenedURLOrm = await session.execute(select(ShortenedURLOrm).where(ShortenedURLOrm.shortened_url==shorted_url))
        orm = orm.scalar()
        if orm is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Url not found")
        return ShortenedURLSchema.model_validate(orm,from_attributes=True)
        