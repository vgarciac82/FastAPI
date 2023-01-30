from app.schemas import User, ShowUser,UserUpdate
from sqlalchemy.orm import Session
from app.db import models

def crear_usuario(usuario:User,db:Session):
    usuario = usuario.dict()
    nuevo_usuario = models.User(
        username=usuario["username"],
        password=usuario["password"],
        nombre=usuario["nombre"],
        apellido=usuario["apellido"],
        telefono=usuario["telefono"],
        correo=usuario["correo"],
        direccion=usuario["direccion"]

    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    
def listar_usuarios(db:Session):
    return db.query(models.User).all()

def obtener_usuario(user_id:str, db:Session):
    usuario = db.query(models.User).filter(models.User.id==user_id).first()
    return usuario

def actualizar_usuario(user_id:int, updateUser: UserUpdate,db:Session):
    usuario = db.query(models.User).filter(models.User.id==user_id)
    
    if not usuario.first():
        return {"respuesta":"usuario no encontrado"}
    
    usuario.update(updateUser.dict(exclude_unset=True) )
    db.commit()
    return {"respuesta":"usuario actualizado"}  

def borrar_usuario(id_usuario:str, db:Session ):
    usuario = db.query(models.User).filter(models.User.id==id_usuario)
    if not usuario.first():
        return {"respuesta":"usuario no encontrado"}
    usuario.delete( synchronize_session = False)
    db.commit()
    return {"respuesta":"usuario eliminado"}
