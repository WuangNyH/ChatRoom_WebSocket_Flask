import re

import bcrypt


def hashPassword(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')


def verifyPassword(hashed, password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))


def checkPassword(password):
    lowercase = bool(re.search("[a-z]", password))
    uppercase = bool(re.search("[A-Z]", password))
    digit = bool(re.search("\d", password))
    special_char = bool(re.search("\W", password))

    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long")

    if not lowercase:
        raise ValueError("Password must contain at least one lowercase letter")

    if not uppercase:
        raise ValueError("Password must contain at least one uppercase letter")

    if not digit:
        raise ValueError("Password must contain at least one digit")

    if not special_char:
        raise ValueError("Password must contain at least one special character")
