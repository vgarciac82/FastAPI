from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas import Login
from app.repository import auth


router = APIRouter(
    prefix="/login",
    tags=["Login"]
)

@router.post("/", status_code=status.HTTP_200_OK)
def login(login:Login, db:Session = Depends(get_db)):
    auth.auth_user(login,db)
    return {"respuesta":"Usuario creado con exito"}
    