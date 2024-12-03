from DB.core import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime
from datetime import datetime

class UserOrm(Base):
    __tablename__ = "users"
    id: Mapped[str] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(nullable=False)
    links: Mapped[list["ShortenedURLOrm"]] = relationship(back_populates="user")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
