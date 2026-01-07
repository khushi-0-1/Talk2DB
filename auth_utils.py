import re
import bcrypt

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()

def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())

def is_valid_password(password: str):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter"
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter"
    if not re.search(r"[0-9]", password):
        return False, "Password must contain at least one digit"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character"
    return True, ""


def is_valid_username(username: str):
    if len(username) < 3 or len(username) > 20:
        return False, "Username must be between 3 and 20 characters"

    if not re.match(r"^[a-zA-Z][a-zA-Z0-9_]*$", username):
        return False, (
            "Username must start with a letter and contain only "
            "letters, numbers, or underscore (_)"
        )

    return True, ""
