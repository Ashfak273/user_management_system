from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

from app.model.user_model import UserRegister, UserLogin, Token, UserUpdate, UserDelete
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

    user = UserRegister(username=username, email=email, password=password)
    return user_service.register_user(user=user, db=db)


@router.post("/login", response_model=Token)
def user_login(db: db_dependency, form_data: OAuth2PasswordRequestForm = Depends()):
    user = UserLogin(username=form_data.username, password=form_data.password)
    return user_service.authenticate_user(user_login=user, db=db)


@router.get("/me/")
def read_users_me(token: Annotated[str, Depends(oauth2_scheme)], db: db_dependency):
    return user_service.get_user_by_token(token, db)


@router.put("/me/")
def update_user(token: Annotated[str, Depends(oauth2_scheme)], db: db_dependency, user_update: UserUpdate):
    return user_service.update_user(token, db, user_update)


@router.delete("/me/")
def delete_user(token: Annotated[str, Depends(oauth2_scheme)], db: db_dependency, user_delete: UserDelete):
    return user_service.delete_user(token, db, user_delete)
