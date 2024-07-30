"""
    User Entity

    This module contains the User class which represents the User entity in the database.

    Author
    ----------
    name: Ashfak Ahamed
    email: mzashfak@gmail.com

    Developers
    ----------
    - name: Ashfak Ahamed
    email: mzashfak@gmail.com

"""
from sqlalchemy import Column, BigInteger, String, DateTime
from sqlalchemy.sql import func

from app.config.database_config import Base


class User(Base):
    """
    User Class

    This class represents the User entity in the database with fields id, username, email, hashed_password, and created_at.

    Attributes:
    ----------
    __tablename__ : str
        The name of the table in the database
    id : Column
        The id of the user, primary key
    username : Column
        The username of the user, must be unique and not null
    email : Column
        The email of the user, must be unique and not null
    hashed_password : Column
        The hashed password of the user, not null
    created_at : Column
        The creation date and time of the user, not null and defaults to the current date and time
    """
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column(String(500), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
