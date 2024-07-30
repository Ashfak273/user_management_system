"""
    User Controller

    This module contains the routes for User related operations.

    Author
    ----------
    name: Ashfak Ahamed
    email: mzashfak@gmail.com

    Developers
    ----------
    - name: Ashfak Ahamed
    email: mzashfak@gmail.com

"""
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

from app.model.user_model import UserRegister, UserLogin, UserUpdate, UserDelete, AuthResponse
from app.config.database_config import db_dependency
from app.service.user_service import UserService

router = APIRouter(
    prefix="/v1/api/users",
    tags=["User"]
)

user_service = UserService()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/api/users/login")


@router.post("/register")
def user_register(db: db_dependency,
                  username: str,
                  email: str,
                  password: str):
    """
    Register a new user.

    Parameters:
    ----------
    db : db_dependency
        The database dependency
    username : str
        The username of the user
    email : str
        The email of the user
    password : str
        The password of the user

    Returns:
    ----------
    The result of the user registration
    """
    user = UserRegister(username=username, email=email, password=password)
    return user_service.register_user(user=user, db=db)


@router.post("/login", response_model=AuthResponse)
def user_login(db: db_dependency, form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Authenticate a user.

    Parameters:
    ----------
    db : db_dependency
        The database dependency
    form_data : OAuth2PasswordRequestForm
        The form data containing the username and password

    Returns:
    ----------
    The result of the user authentication
    """
    user = UserLogin(username=form_data.username, password=form_data.password)
    return user_service.authenticate_user(user_login=user, db=db)


@router.get("/me")
def read_users_me(token: Annotated[str, Depends(oauth2_scheme)], db: db_dependency):
    """
       Get the user by token.

       Parameters:
       ----------
       token : str
           The token of the user
       db : db_dependency
           The database dependency

       Returns:
       ----------
       The user associated with the token
       """
    return user_service.get_user_by_token(token, db)


@router.put("/me")
def update_user(token: Annotated[str, Depends(oauth2_scheme)], db: db_dependency, user_update: UserUpdate):
    """
    Update a user.

    Parameters:
    ----------
    token : str
        The token of the user
    db : db_dependency
        The database dependency
    user_update : UserUpdate
        The user update data

    Returns:
    ----------
    The result of the user update
    """
    return user_service.update_user(token, db, user_update)


@router.delete("/me")
def delete_user(token: Annotated[str, Depends(oauth2_scheme)], db: db_dependency, user_delete: UserDelete):
    """
    Delete a user.

    Parameters:
    ----------
    token : str
        The token of the user
    db : db_dependency
        The database dependency
    user_delete : UserDelete
        The user delete data

    Returns:
    ----------
    The result of the user deletion
    """
    return user_service.delete_user(token, db, user_delete)
