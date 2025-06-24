from sqlalchemy import text
from app.database import engine

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Conexao bem sucedida")
except Exception as e:
    print("Erro ao conectar: ", e)