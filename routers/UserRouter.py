from fastapi import APIRouter
from Schemas.UserSchemas import SignUpSchema,UserSchema
from DB.Repos.UserRepository import create_user
router = APIRouter(tags=["Users"])


@router.post("/signup")
async def signup(user: SignUpSchema) -> UserSchema:
    user_schema: UserSchema = await create_user(user)
    return user_schema
