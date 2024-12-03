from DB.core import session_maker
from Schemas.UserSchemas import SignUpSchema, UserSchema
from DB.ORMs.UserOrm import UserOrm
from uuid import uuid4
from datetime import datetime,timezone
from utils import hash_password


async def create_user(user: SignUpSchema) -> UserSchema:
    async with session_maker.begin() as session:
        user_orm: UserOrm = UserOrm(
            id=str(uuid4()),
            username=user.username,
            password=hash_password(user.password),
            email=user.email,
            is_active=False,
            created_at=datetime.now(timezone.utc),
            links=[]
        )
    session.add(user_orm)
    await session.commit()
    return UserSchema.model_validate(user_orm,from_attributes=True)

async def activate_user() -> UserSchema:
    