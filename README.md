# FastAPI


python -m venv .\env
.\env\Scripts\activate
pip install -r .\requirements.txt
alembic upgrade head

#Comando para ver la completitud de las pruebas.
coverage run -m pytest
coverage html