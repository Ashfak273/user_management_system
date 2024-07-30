import jwt
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone

from app.service.http_service import logger
from app.model.generic_response import GenericResponse
from app.repository.user_repository import UserRepository

load_dotenv('.env')
SECRET_KEY = os.environ.get('SECRET_KEY', 'UserManagementSystem273')
ALGORITHM = "HS256"


def create_access_token(user):
    payload = {
        "sub": user.id,
        "exp": datetime.now(timezone.utc) + timedelta(days=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


def get_current_user(token, db):
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
