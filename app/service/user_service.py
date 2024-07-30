"""
    User Service

    This module contains the UserService class for handling user related operations.

    Author
    ----------
    name: Ashfak Ahamed
    email: mzashfak@gmail.com

    Developers
    ----------
    - name: Ashfak Ahamed
    email: mzashfak@gmail.com

"""
import re
from datetime import datetime
from passlib.context import CryptContext

from app.model.user_model import UserRegister, UserLogin, UserUpdate, UserDelete, AuthResponse
from app.repository.user_repository import UserRepository
from app.entity.user_entity import User
from app.model.generic_response import GenericResponse
from app.util.auth import create_access_token, get_current_user
from app.config.logging_config import get_logger

logger = get_logger(class_name=__name__)


class UserService:
    """
    UserService Class

    This class is used to handle user related operations such as registration, authentication, getting user by token,
    updating user, and deleting user.

    Attributes:
    ----------
    pwd_context : CryptContext
        The password context for hashing passwords
    """
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def register_user(cls, user: UserRegister, db):
        """
        Register a new user.

        Parameters:
        ----------
        user : UserRegister
            The user registration data
        db : db_dependency
            The database dependency

        Returns:
        ----------
        The result of the user registration
        """
        try:
            logger.info("User Registration Started")
            user_in_db = UserRepository.get_user_by_username(db, user.username)

            if user_in_db:
                logger.info("Username already exists")
                return GenericResponse.failed(message="Username already exists", results=[])

            email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if not re.fullmatch(email_regex, user.email):
                logger.info("Invalid email format")
                return GenericResponse.failed(message="Invalid email format", results=[])

            hashed_password = cls.pwd_context.hash(user.password)
            created_at = datetime.now()
            new_user = User(username=user.username, email=user.email,
                            hashed_password=hashed_password, created_at=created_at)
            user_details = UserRepository.create_user(db, new_user)

            logger.info("User Registered Successfully")
            return GenericResponse.success(message="User Registered Successfully", results=user_details)
        except Exception as e:
            logger.error(f"Error in User Registration: {str(e)}")
            logger.info("User Registration Failed")
            return GenericResponse.failed(message=f"User Registration Failed : {str(e)}", results=[])

    @classmethod
    def authenticate_user(cls, user_login: UserLogin, db):
        """
        Authenticate a user.

        Parameters:
        ----------
        user_login : UserLogin
            The user login data
        db : db_dependency
            The database dependency

        Returns:
        ----------
        The result of the user authentication
        """
        try:
            logger.info("User Authentication Started")
            user = UserRepository.get_user_by_username(db, user_login.username)
            if not user or not cls.pwd_context.verify(user_login.password, user.hashed_password):
                logger.info("Invalid Credentials")
                return AuthResponse(success=False, message="Invalid Credentials / User Not Found")

            token = create_access_token(user)
            logger.info("User Authenticated Successfully created")
            return AuthResponse(access_token=token, token_type="bearer", success=True,
                                message="User Authenticated Successful", )
        except Exception as e:
            logger.error(f"Error in User Authentication: {str(e)}")
            logger.info("User Authentication Failed")
            return AuthResponse(success=False, message=f"User Authentication Failed : {str(e)}")

    @classmethod
    def get_user_by_token(cls, token, db):
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
        try:
            logger.info("Get User By Token Started")
            user, _ = get_current_user(token, db)

            if not user:
                logger.info("User Not Found.")
                return GenericResponse.failed(message="User Not Found.", results=[])

            logger.info("User Found")
            return GenericResponse.success(message="User Found",
                                           results={"username": user.username, "email": user.email})
        except Exception as e:
            logger.error(f"Error in Get User By Token: {str(e)}")
            logger.info("Get User By Token Failed")
            return GenericResponse.failed(message=f"Get User By Token Failed : {str(e)}", results=[])

    @classmethod
    def update_user(cls, token, db, user_update: UserUpdate):
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
        try:
            logger.info("Update User Started")
            user, _ = get_current_user(token, db)

            if not user:
                logger.info("User Not Found")
                return GenericResponse.failed(message="User Not Found", results=[])

            if user_update.username is None and user_update.email is None and user_update.password is None:
                logger.info("Username, Email and Password are missing.")
                return GenericResponse.failed(message="Username, Email and Password are missing.", results=[])

            if user_update.password:
                hashed_password = cls.pwd_context.hash(user_update.password)
                user_update.password = hashed_password

            updated_user = UserRepository.update_user(db, user, user_update)
            logger.info("User Updated Successfully")
            return GenericResponse.success(message="User Updated Successfully",
                                           results={"username": updated_user.username, "email": updated_user.email})
        except Exception as e:
            logger.error(f"Error in Update User: {str(e)}")
            logger.info("Update User Failed")
            return GenericResponse.failed(message=f"Update User Failed : {str(e)}", results=[])

    @classmethod
    def delete_user(cls, token, db, user_delete: UserDelete):
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
        try:
            logger.info("Delete User Started")
            user, user_id = get_current_user(token, db)

            if user.username != user_delete.username:
                logger.info("Username Does not match with authenticated user.")
                return GenericResponse.failed(message="Username Does not match with authenticated user.", results=[])

            UserRepository.delete_user_by_id(db, user_id)
            logger.info("User Deleted Successfully")
            return GenericResponse.success(message="User Deleted Successfully", results=[])
        except Exception as e:
            logger.error(f"Error in Delete User: {str(e)}")
            logger.info("Delete User Failed")
            return GenericResponse.failed(message=f"Delete User Failed : {str(e)}", results=[])
