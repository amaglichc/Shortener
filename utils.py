from string import ascii_letters, digits
from random import choice
import bcrypt


def generate_short_url(length=6, chars=ascii_letters + digits):
    return "".join(choice(chars) for _ in range(length))


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_pasword = bcrypt.hashpw(password.encode(), salt)
    return hashed_pasword.decode()


def check_password(password: str, hashed_pasword: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed_pasword.encode())
