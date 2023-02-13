from sqlalchemy import create_engine,insert
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from main import app
from app.db.database import engine
from app.db.models import Base, User
from app.hashing import Hash
from app.db.database import get_db

db_path = os.path.join(os.path.dirname(__file__),'test.db')
db_uri = "sqlite:///{}".format(db_path)

engine = create_engine(db_uri)
Base.metadata.create_all(bind=engine)
TestingSessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)


def crea_primer_usuario():
    password_hash = Hash.hash_password('perote')
    
    Session = sessionmaker(bind=engine)
    session = Session()
    usuario = User(
        nombre="cherlo", 
        username="cherlo56",
        password=password_hash, 
        apellido="garcia",
        direccion="conocida", 
        telefono="3335",
        correo="cherlo56@latinchat.com" 
    )
    session.add(usuario)
    session.commit()
    session.close()

crea_primer_usuario()


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
app.dependency_overrides[get_db] = override_get_db

cliente = TestClient(app)


def test_crear_usuario():
    usuario = {
        "username": "cherlux",
        "password": "12345678",
        "nombre": "Vicente",
        "apellido": "Garcia",
        "direccion": "Conocida",
        "telefono": 3335588,
        "correo": "cherlux@gmail.com",
        "creacion": "2023-02-07T06:38:00.785759"
    }

    response = cliente.post("/user/crear_usuario", json=usuario)
    
    print( response, dir(response),"status code", response.status_code )
    print(response.json())

    assert response.status_code == 401
    
    
    usuarioTest = {
        "username": "cherlo56",
        "password": "perote"
    }
    
    response_token = cliente.post("/login/",data=usuarioTest)
    assert response_token.status_code == 200
    assert response_token.json()["token_type"] == "bearer"
    
    headers = {
        "Authorization": "Bearer {}".format(response_token.json()["access_token"])
    }
    print( headers )
    response = cliente.post("/user/crear_usuario", json=usuario, headers=headers)
    print(response)

    assert response.status_code == 201

def test_obtener_usuarios():
    usuarioTest = {
        "username": "cherlo56",
        "password": "perote"
    }
    
    response_token = cliente.post("/login/",data=usuarioTest)
    assert response_token.status_code == 200
    assert response_token.json()["token_type"] == "bearer"
   
    headers = {
        "Authorization": "Bearer {}".format(response_token.json()["access_token"])
    }
    
    response = cliente.get("/user/", headers=headers)
    
    assert response.status_code == 200
    assert len(response.json())==2
     
def test_obtener_usuario():
    response = cliente.get("/user/1")
    print(response.json())
    assert response.status_code == 200
    assert response.json()["username"] == "cherlo56"

def test_eliminar_usuario():
    response = cliente.delete("/borrar/2")
    print(response.json())
    assert response.status_code == 404
    
def test_actualizar_usuario():
    usuario = {
        "username" : "cherlo82",
    }
    
    response = cliente.patch("/user/1", json=usuario)
    print("====================================================== Resultado de la actualizacion ======================================================")
    print(response)
    assert response.status_code == 202
    


def test_delete_database():
    db_path = os.path.join(os.path.dirname(__file__),'test.db')
    os.remove(db_path)
    
