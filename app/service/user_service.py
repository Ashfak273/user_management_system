import os

from passlib.context import CryptContext
from app.model.user_model import UserRegister, UserLogin
from app.repository.user_repository import UserRepository
from app.entity.user_entity import User
from app.service.http_service import logger
from app.model.generic_response import GenericResponse
from dotenv import load_dotenv
from app.model.user_model import Token

import jwt
from datetime import datetime, timedelta, timezone


class UserService:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    load_dotenv('.env')
    secret_key = os.environ.get('SECRET_KEY', 'UserManagementSystem273')

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

            payload = {
                "sub": user.id,
                "exp": datetime.now(timezone.utc) + timedelta(days=1)
            }

            token = jwt.encode(payload, cls.secret_key, algorithm="HS256")
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
            payload = jwt.decode(token, cls.secret_key, algorithms=["HS256"])
            print("payload", payload)
            user_id = payload.get("sub")
            print("user_id", user_id)
            if not user_id:
                logger.info("Invalid Token")
                return GenericResponse.failed(message="Invalid Token", results=[])

            user = UserRepository.get_user_by_id(db, user_id)

            if not user:
                logger.info("User Not Found")
                return GenericResponse.failed(message="User Not Found", results=[])

            logger.info("User Found")
            return GenericResponse.success(message="User Found", results={"username": user.username, "email": user.email})
        except Exception as e:
            logger.error(f"Error in Get User By Token: {str(e)}")
            logger.info("Get User By Token Failed")
            return GenericResponse.failed(message=f"Get User By Token Failed : {str(e)}", results=[])