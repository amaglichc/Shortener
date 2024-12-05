from DB.core import session_maker
from Schemas.UserSchemas import SignUpSchema, UserSchema, SignInSchema
from DB.ORMs.UserOrm import UserOrm
from uuid import uuid4
from datetime import datetime, timezone
from utils import hash_password, check_password
from sqlalchemy import select
from exceptions import UserNotFoundException, InvalidCredentialsException


async def create_user(user: SignUpSchema) -> UserSchema:
    async with session_maker.begin() as session:
        user_orm: UserOrm = UserOrm(
            id=str(uuid4()),
            username=user.username,
            password=hash_password(user.password),
            email=user.email,
            is_active=False,
            created_at=datetime.now(timezone.utc),
            links=[],
        )
    session.add(user_orm)
    await session.commit()
    return UserSchema.model_validate(user_orm, from_attributes=True)


async def check_user_access(user: SignInSchema):
    async with session_maker.begin() as session:
        user_orm = (
            await session.execute(select(UserOrm).where(UserOrm.email == user.email))
        ).scalar()
        if user_orm is None:
            raise UserNotFoundException
        if check_password(user.password, user_orm.password):
            return True,user_orm
        raise InvalidCredentialsException


# async def activate_user() -> UserSchema:
