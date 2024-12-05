from pydantic_settings import BaseSettings
import jwt
from pathlib import Path
from copy import deepcopy
from datetime import datetime, timezone, timedelta
from Schemas.UserSchemas import UserSchema
from Schemas.TokenSchemas import TokenSchema

cwd = Path.cwd()


class TokenConfig(BaseSettings):
    private_key: str = (cwd / "certs" / "private_key.pem").read_text()
    public_key: str = (cwd / "certs" / "public_key.pem").read_text()
    ALGORITHM: str = "RS256"
    EXPIRE_MINUTES_ACCESS: int = 5
    EXPIRE_MINUTES_REFRESH: int = 7 * 24 * 60


token_config = TokenConfig()


def create_token(
    data: dict,
    expire_mins: int = token_config.EXPIRE_MINUTES_ACCESS,
    key=token_config.private_key,
    alg=token_config.ALGORITHM,
):
    new_data = deepcopy(data)
    now: datetime = datetime.now(timezone.utc)
    new_data["iat"] = now
    new_data["exp"] = now + timedelta(minutes=expire_mins)
    return jwt.encode(new_data, key, alg)


def decode_token(token: str, key=token_config.public_key, alg=token_config.ALGORITHM):
    return jwt.decode(token, key, algorithms=alg)


def create_access_token(user: UserSchema) -> str:
    data = {"sub": user.id, "is_active": user.is_active}
    return create_token(data)


def create_refresh_token(user: UserSchema) -> str:
    data = {"sub": user.id, "is_active": user.is_active}
    return create_token(data, expire_mins=token_config.EXPIRE_MINUTES_REFRESH)


def create_tokens(user: UserSchema) -> TokenSchema:
    access = create_access_token(user)
    refresh = create_refresh_token(user)
    return TokenSchema(access_token=access, refresh_token=refresh)
