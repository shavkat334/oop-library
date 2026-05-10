from string import digits


def validate_username(username: str) -> tuple[bool, str]:
    if " " in username:
        return False, "Username bo'sh jouydan iborat bo'lmaslik kerak."
    elif not username.isalpha():
        return False, "Username harflar iborat bo'lishi kerak."
    elif not username.islower():
        return False, "Username kichik harflardan iborat bo'lishi kerak."
    else:
        return True, ""


import re
import string

def validate_password(password: str) -> tuple[bool, str]:
    if len(password) < 4:
        return False, "Password kamida 4 ta belgidan iborat bo'lsin"

    if not any(ch.isdigit() for ch in password):
        return False, "Password kamida 1 ta raqamdan iborat bo'lsin"

    return True, ""

def validate_email(email: str) -> tuple[bool, str]:
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    if not re.match(pattern, email):
        return False, "Email manzili noto'g'ri formatda."
    return True, ""

def normalize_full_name(full_name: str) -> str:
    return full_name.title()
