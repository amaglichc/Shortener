from datetime import datetime
from DB.core import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime


class ShortenedURLOrm(Base):
    __tablename__ = "urls"
    id: Mapped[str] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(nullable=False)
    shortened_url: Mapped[str] = mapped_column(unique=True, nullable=False)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    user: Mapped["UserOrm"] = relationship(back_populates="links")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )
    expires_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )
