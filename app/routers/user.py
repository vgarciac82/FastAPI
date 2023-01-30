from fastapi import APIRouter,Depends
from app.schemas import User, ShowUser,UserUpdate
from app.db.database import get_db
from sqlalchemy.orm import Session
from typing import List
from app.repository import User_Repository

router = APIRouter(
    prefix="/user", 
    tags = ["Users"]
)
 
@router.post('/crear_usuario')
def crear_usuario(user:User,db:Session = Depends(get_db)):
    User_Repository.crear_usuario(user,db)
    return {"respuesta":"Usuario creado con exito"}

@router.get("/",response_model=List[ShowUser])
def listar_usuarios(db:Session = Depends(get_db)):
    data = User_Repository.listar_usuarios(db)
    return data;

@router.get("/{user_id}", response_model=ShowUser)
def obtener_usuario(user_id:str, db:Session = Depends(get_db)):
    usuario = User_Repository.obtener_usuario(user_id, db)
    if not usuario:
        return {"respuesta":"usuario no encontrado"}
    return usuario


@router.patch("/{user_id}")
def actualizar_usuario(user_id:int, updateUser: UserUpdate,db:Session = Depends(get_db) ):
    response = User_Repository.actualizar_usuario(user_id, updateUser,db)
    return response
 
@router.delete('/borrar/{id_usuario}')
def borrar_usuario(id_usuario:str, db:Session = Depends(get_db)):
   response = User_Repository.borrar_usuario(id_usuario, db)
   return response
