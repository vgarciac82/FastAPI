from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db

router = APIRouter(
    prefix="/login",
    tags=["Login"]
)

@router.get("/", status_code=status.HTTP_200_OK)
def login(db:Session = Depends(get_db)):
    return {"res":"login aceptado"}
    