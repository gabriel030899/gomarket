from fastapi import FastAPI
from app.database import engine, Base
from app.models import user, market, product, price, receipt

app = FastAPI()

# Cria as tabelas no banco de dados ( basedo no models )
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"msg": "GoMarket API funcionando"}