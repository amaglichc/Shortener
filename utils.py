from string import ascii_letters, digits
from random import choice


def generate_short_url(length=6, chars=ascii_letters + digits):
    return "".join(choice(chars) for _ in range(length))
