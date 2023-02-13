from fastapi import APIRouter,Depends,status
from app.schemas import User, ShowUser,UserUpdate
from app.db.database import get_db
from sqlalchemy.orm import Session
from typing import List
from app.repository import User_Repository
from app.oauth import get_current_user

router = APIRouter(
    prefix="/user", 
    tags = ["Users"]
)
 
@router.post('/crear_usuario',status_code=status.HTTP_201_CREATED)
def crear_usuario(user:User,db:Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    User_Repository.crear_usuario(user,db)
    return {"respuesta":"Usuario creado con exito"}
    

@router.get('/',response_model=List[ShowUser],status_code=status.HTTP_200_OK)
def obtener_usuarios(db:Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    data = User_Repository.listar_usuarios(db)
    return data

@router.get("/{user_id}", response_model=ShowUser )
def obtener_usuario(user_id:str, db:Session = Depends(get_db)):
    usuario = User_Repository.obtener_usuario(user_id, db)
    if not usuario:
        return {"respuesta":"usuario no encontrado"}
    return usuario


@router.patch("/{user_id}",status_code=status.HTTP_202_ACCEPTED)
def actualizar_usuario(user_id:int, updateUser: UserUpdate,db:Session = Depends(get_db) ):
    response = User_Repository.actualizar_usuario(user_id, updateUser,db)
    return response
 
@router.delete('/borrar/{id_usuario}',status_code=status.HTTP_200_OK)
def borrar_usuario(id_usuario:str, db:Session = Depends(get_db)):
   response = User_Repository.borrar_usuario(id_usuario, db)
   return response
