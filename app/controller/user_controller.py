from fastapi import APIRouter, HTTPException


router = APIRouter(
    prefix="/v1/api/user",
    tags=["User"]
)


@router.get("/")
def read_root():
    return {"Hello World": "User Management System"}
