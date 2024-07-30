"""
    Auth Utility

    This module contains utility functions for handling authentication related operations such as creating access
    tokens and getting the current user from a token.

    Author
    ----------
    name: Ashfak Ahamed
    email: mzashfak@gmail.com

    Developers
    ----------
    - name: Ashfak Ahamed
    email: mzashfak@gmail.com

"""
import jwt
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone

from app.model.generic_response import GenericResponse
from app.repository.user_repository import UserRepository
from app.config.logging_config import get_logger

logger = get_logger(class_name=__name__)

load_dotenv('.env')
SECRET_KEY = os.environ.get('SECRET_KEY', 'UserManagementSystem273')
ALGORITHM = "HS256"


def create_access_token(user):
    """
    Create an access token for a user.

    Parameters:
    ----------
    user : User
        The user for which to create the access token

    Returns:
    ----------
    str
        The created access token
    """
    payload = {
        "sub": user.id,
        "exp": datetime.now(timezone.utc) + timedelta(days=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


def get_current_user(token, db):
    """
       Get the current user from a token.

       Parameters:
       ----------
       token : str
           The token of the user
       db : db_dependency
           The database dependency

       Returns:
       ----------
       User, int
           The user associated with the token and the user id
       """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        user_id = payload.get("sub")
        if not user_id:
            logger.info("User ID not found from token")
            return GenericResponse.failed(message="User ID not found from token", results=[])

        user = UserRepository.get_user_by_id(db, user_id)
        return user, user_id
    except jwt.PyJWTError:
        logger.info("Invalid Token.")
        return GenericResponse.failed(message="Invalid Token", results=[])
