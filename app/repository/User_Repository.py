from app.schemas import User, ShowUser,UserUpdate
from sqlalchemy.orm import Session
from app.db import models
from fastapi import  HTTPException,status
from app.hashing import Hash



def crear_usuario(usuario:User,db:Session):
    try:
        usuario = usuario.dict()
        nuevo_usuario = models.User(
            username=usuario["username"],
            password= Hash.hash_password( usuario["password"] ),
            nombre=usuario["nombre"],
            apellido=usuario["apellido"],
            telefono=usuario["telefono"],
            correo=usuario["correo"],
            direccion=usuario["direccion"]

        )
        db.add(nuevo_usuario)
        db.commit()
        db.refresh(nuevo_usuario)
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creando usuario {e}"
        )
        
def listar_usuarios(db:Session):
    return db.query(models.User).all()

def obtener_usuario(user_id:str, db:Session):
    usuario = db.query(models.User).filter(models.User.id==user_id).first()
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se encontro usuario con ID {user_id}"
        )
    return usuario

def actualizar_usuario(user_id:int, updateUser: UserUpdate,db:Session):
    usuario = db.query(models.User).filter(models.User.id==user_id)
    
    if not usuario.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se encontro usuario con ID {user_id}"
        )
    
    usuario.update(updateUser.dict(exclude_unset=True) )
    db.commit()
    return {"respuesta":"usuario actualizado"}  

def borrar_usuario(id_usuario:str, db:Session ):
    usuario = db.query(models.User).filter(models.User.id==id_usuario)
    if not usuario.first():
       raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se encontro usuario con ID {id_usuario}"
        )
    usuario.delete( synchronize_session = False)
    db.commit()
    return {"respuesta":"usuario eliminado"}
