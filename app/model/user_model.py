"""
    User Models

    This module contains the Pydantic models for User related operations.

    Author
    ----------
    name: Ashfak Ahamed
    email: mzashfak@gmail.com

    Developers
    ----------
    - name: Ashfak Ahamed
    email: mzashfak@gmail.com

"""
from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserRegister(BaseModel):
    """
    UserRegister Model

    Attributes:
    ----------
    username : str
        The username of the user
    email : EmailStr
        The email of the user
    password : str
        The password of the user
    """
    username: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    """
    UserLogin Model

    Attributes:
    ----------
    username : str
        The username of the user
    password : str
        The password of the user
    """
    username: str
    password: str


class AuthResponse(BaseModel):
    """
    AuthResponse Model

    Attributes:
    ----------
    access_token : Optional[str]
        The access token of the user
    token_type : Optional[str]
        The type of the token
    success : bool
        The success status of the authentication
    message : Optional[str]
        The message of the authentication response
    """
    access_token: Optional[str] = None
    token_type: Optional[str] = None
    success: bool
    message: Optional[str] = None


class UserUpdate(BaseModel):
    """
    UserUpdate Model

    Attributes:
    ----------
    username : Optional[str]
        The username of the user
    email : Optional[str]
        The email of the user
    password : Optional[str]
        The password of the user
    """
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None


class UserDelete(BaseModel):
    """
    UserDelete Model

    Attributes:
    ----------
    username : str
        The username of the user
    """
    username: str
