from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class AuthResponse(BaseModel):
    access_token: Optional[str] = Field(None)
    token_type: Optional[str] = Field(None)
    success: bool = Field(...)
    message: Optional[str] = Field(None)


class UserUpdate(BaseModel):
    username: Optional[str] = Field(None)
    email: Optional[str] = Field(None)
    password: Optional[str] = Field(None)


class UserDelete(BaseModel):
    username: str
