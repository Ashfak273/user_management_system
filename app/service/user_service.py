from passlib.context import CryptContext

from app.model.user_model import UserRegister, UserLogin, UserUpdate, UserDelete
from app.repository.user_repository import UserRepository
from app.entity.user_entity import User
from app.service.http_service import logger
from app.model.generic_response import GenericResponse
from app.model.user_model import Token
from app.util.auth import create_access_token, get_current_user


class UserService:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def register_user(cls, user: UserRegister, db):
        try:
            logger.info("User Registration Started")
            user_in_db = UserRepository.get_user_by_username(db, user.username)

            if user_in_db:
                logger.info("Username already exists")
                return GenericResponse.failed(message="Username already exists", results=user_in_db)

            hashed_password = cls.pwd_context.hash(user.password)
            new_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
            user_details = UserRepository.create_user(db, new_user)

            logger.info("User Registered Successfully")
            return GenericResponse.success(message="User Registered Successfully", results=user_details)
        except Exception as e:
            logger.error(f"Error in User Registration: {str(e)}")
            logger.info("User Registration Failed")
            return GenericResponse.failed(message=f"User Registration Failed : {str(e)}", results=[])

    @classmethod
    def authenticate_user(cls, user_login: UserLogin, db):
        try:
            logger.info("User Authentication Started")
            user = UserRepository.get_user_by_username(db, user_login.username)
            if not user or not cls.pwd_context.verify(user_login.password, user.hashed_password):
                logger.info("Invalid Credentials")
                return GenericResponse.failed(message="Invalid Credentials", results=[])

            token = create_access_token(user)
            logger.info("User Authenticated Successfully created")
            return Token(access_token=token, token_type="bearer")
        except Exception as e:
            logger.error(f"Error in User Authentication: {str(e)}")
            logger.info("User Authentication Failed")
            return GenericResponse.failed(message=f"User Authentication Failed : {str(e)}", results=[])

    @classmethod
    def get_user_by_token(cls, token, db):
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
        try:
            logger.info("Update User Started")
            user, _ = get_current_user(token, db)

            if not user:
                logger.info("User Not Found")
                return GenericResponse.failed(message="User Not Found", results=[])

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
