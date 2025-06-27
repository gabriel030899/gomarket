from fastapi import FastAPI
from app.database import engine, Base
from app.models import user, market, product, price, receipt
from app.routers import product, market, user




app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Para desenvolvimento. Depois coloque só os domínios necessários!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Cria as tabelas no banco de dados ( basedo no models )
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"msg": "GoMarket API funcionando"}

app.include_router(product.router)
app.include_router(market.router)
app.include_router(user.router)