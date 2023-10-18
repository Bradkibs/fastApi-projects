# pylint: disable=all

import re

from pydantic import BaseModel, EmailStr, constr, validator
from enum import Enum


class RoleChoices(str, Enum):
    USER = 'user'
    CUSTOMER_SERVICE = 'customer_service'
    ADMIN = 'admin'


class RegisterUserRequest(BaseModel):
    email: EmailStr
    password: constr(min_length=8, max_length=64, strict=True)
    username: constr(min_length=3, max_length=64, strict=True)
    phone_number: constr(min_length=10, max_length=14, strip_whitespace=True, strict=True)
    location: constr(min_length=2, max_length=20, strip_whitespace=True, strict=True)
    role: RoleChoices

    @validator("password")
    def password_must_contain_special_characters(cls, v):
        if not re.search(r"[^a-zA-Z0-9]", v):
            raise ValueError("Password must contain special characters")
        return v

    @validator("password")
    def password_must_contain_numbers(cls, v):
        if not re.search(r"[0-9]", v):
            raise ValueError("Password must contain numbers")
        return v

    @validator("password")
    def password_must_contain_uppercase(cls, v):
        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain uppercase characters")
        return v

    @validator("password")
    def password_must_contain_lowercase(cls, v):
        if not re.search(r"[a-z]", v):
            raise ValueError("Password must contain lowercase characters")
        return v

    @validator("username")
    def username_must_not_contain_special_characters(cls, v):
        if re.search(r"[^a-zA-Z0-9]", v):
            raise ValueError("Username must not contain special characters")
        return v

    @validator("phone_number")
    def phone_number_must_contain_plus_then_numbers(cls, v):
        if not re.search(r"^\+\d+$", v):
            raise ValueError("Phone number must start with + and then numbers")
        return v


class LoginUserRequest(BaseModel):
    phone_number: constr(min_length=10, max_length=14, strip_whitespace=True, strict=True)
    email: EmailStr
    password: constr(min_length=8, max_length=64, strict=True)



    @validator("phone_number")
    def phone_number_must_contain_plus_then_numbers(cls, v):
        if not re.search(r"^\+\d+$", v):
            raise ValueError("Phone number must start with + and then numbers")
        return v
