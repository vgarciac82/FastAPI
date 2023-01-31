from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    
    def hash_password(str_pwd):
        return pwd_context.hash(str_pwd)