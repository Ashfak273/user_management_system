"""
    User Repository

    This module contains the UserRepository class for handling database operations related to the User entity.

    Author
    ----------
    name: Ashfak Ahamed
    email: mzashfak@gmail.com

    Developers
    ----------
    - name: Ashfak Ahamed
    email: mzashfak@gmail.com

"""
from sqlalchemy.orm import Session

from app.entity.user_entity import User
from app.exceptions.db_operation_exception import DbOperationException


class UserRepository:
    """
    UserRepository Class

    This class is used to handle database operations related to the User entity such as getting user by username,
    creating a user, getting user by id, updating a user, and deleting a user by id.

    """

    @staticmethod
    def get_user_by_username(db: Session, username: str):
        """
        Get a user by username.

        Parameters:
        ----------
        db : Session
            The database session
        username : str
            The username of the user

        Returns:
        ----------
        The user associated with the username
        """
        try:
            return db.query(User).filter(User.username == username).first()
        except Exception as e:
            raise DbOperationException(str(e), e)

    @staticmethod
    def create_user(db: Session, user: User):
        """
        Create a new user.

        Parameters:
        ----------
        db : Session
            The database session
        user : User
            The user data

        Returns:
        ----------
        The created user
        """
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
        """
        Get a user by id.

        Parameters:
        ----------
        db : Session
            The database session
        user_id : int
            The id of the user

        Returns:
        ----------
        The user associated with the id
        """
        try:
            return db.query(User).filter(User.id == user_id).first()
        except Exception as e:
            raise DbOperationException(str(e), e)

    @staticmethod
    def update_user(db: Session, user: User, user_update):
        """
        Update a user.

        Parameters:
        ----------
        db : Session
            The database session
        user : User
            The current user data
        user_update : UserUpdate
            The user update data

        Returns:
        ----------
        The updated user
        """
        try:
            if user_update.username:
                user.username = user_update.username
            if user_update.email:
                user.email = user_update.email
            if user_update.password:
                user.hashed_password = user_update.password
            db.commit()
            return user
        except Exception as e:
            db.rollback()
            raise DbOperationException(str(e), e)

    @staticmethod
    def delete_user_by_id(db: Session, user_id: int):
        """
        Delete a user by id.

        Parameters:
        ----------
        db : Session
            The database session
        user_id : int
            The id of the user

        Returns:
        ----------
        None
        """
        try:
            user = db.query(User).filter(User.id == user_id).first()
            db.delete(user)
            db.commit()
        except Exception as e:
            db.rollback()
            raise DbOperationException(str(e), e)
