from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABSE_URL = "postgresql://alestra:alestra@localhost:5432/usuarios"
engine = create_engine(SQLALCHEMY_DATABSE_URL)
SessionLocal = sessionmaker(bind = engine, autocommit = False, autoflush=False)
Base = declarative_base()

def get_db():
        db  = SessionLocal()
        try:
            yield db
        finally :
            db.close()