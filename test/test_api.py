from fastapi.testclient import TestClient
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from main import app

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

    assert response.status_code == 201
