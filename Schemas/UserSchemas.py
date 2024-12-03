from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from Schemas.URLShemas import ShortenedURLSchema


class SignUpSchema(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    email: EmailStr
    password: str = Field(min_length=5, max_length=30)


class SignInSchema(BaseModel):
    email: EmailStr
    password: str


class UserSchema(BaseModel):
    id: str
    username: str
    password: str
    email: EmailStr
    created_at: datetime
    is_active: bool = False
    links: list[ShortenedURLSchema] = []
