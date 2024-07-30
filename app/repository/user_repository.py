from sqlalchemy.orm import Session
from app.entity.user_entity import User
from app.exceptions.db_operation_exception import DbOperationException


class UserRepository:

    @staticmethod
    def get_user_by_username(db: Session, username: str):
        try:
            return db.query(User).filter(User.username == username).first()
        except Exception as e:
            raise DbOperationException(str(e), e)

    @staticmethod
    def create_user(db: Session, user: User):
        try:
            db.add(user)
            db.commit()
            db.refresh(user)
            return user
        except Exception as e:
            db.rollback()
            raise DbOperationException(str(e), e)

    @staticmethod
    def get_user_by_id(db: Session, user_id: int):
        try:
            return db.query(User).filter(User.id == user_id).first()
        except Exception as e:
            raise DbOperationException(str(e), e)
