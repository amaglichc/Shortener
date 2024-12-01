from datetime import datetime
from DB.core import Base
from sqlalchemy.orm import Mapped, mapped_column


class ShortenedURLOrm(Base):
    id: Mapped[str] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(nullable=False)
    shortened_url: Mapped[str] = mapped_column(unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(nullable=False)
    expires_at: Mapped[datetime] = mapped_column(nullable=False)
