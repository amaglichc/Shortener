from fastapi import APIRouter
from Schemas.UserSchemas import SignUpSchema, UserSchema, SignInSchema
from Schemas.TokenSchemas import TokenSchema
from DB.Repos.UserRepository import create_user, check_user_access
from auth_jwt import create_tokens


router = APIRouter(tags=["Auth"])


@router.post("/signup")
async def signup(user: SignUpSchema) -> UserSchema:
    user_schema: UserSchema = await create_user(user)
    return user_schema


@router.post("/signin")
async def signin(user: SignInSchema) -> TokenSchema:
    flag,user_orm = await check_user_access(user)
    if flag:
        return create_tokens(user_orm)
