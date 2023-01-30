from fastapi import FastAPI
import uvicorn
from app.routers import user
from app.db.database import Base,engine

app = FastAPI()

app.include_router(user.router)


def create_tables():
    print("Creando tablas en la base de datos")
    Base.metadata.create_all(bind = engine)
    print("Tablas creadas")

create_tables()

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
