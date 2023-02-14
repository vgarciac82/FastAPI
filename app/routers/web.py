from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

router = APIRouter(
     
)
 
 
templates = Jinja2Templates(directory="app/templates")

@router.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@router.get("/register")
def registration(request: Request):
    return templates.TemplateResponse("crear_usuario.html", {"request": request})


@router.post("/register")
async def registration(request: Request):
    form = await request.form()
    usuario = {
        "username" : form.get("username"),
        "password" : form.get("password"),
        "nombre" : form.get("nombre"),
        "apellido" : form.get("apellido"),
        "correo" : form.get("correo"),
        "telefono" : form.get("telefono"),
        "direccion" : form.get("direccion"),
    }
    print(usuario)
    return templates.TemplateResponse("crear_usuario.html", {"request": request})

