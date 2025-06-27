from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import models
from app.schemas import market as market_schema
from app.database import SessionLocal

router = APIRouter(
    prefix="/markets",
    tags=["Markets"]
)

# Dependência para obter a sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET → Listar todos os mercados
@router.get("/", response_model=List[market_schema.Market])
def get_markets(db: Session = Depends(get_db)):
    markets = db.query(models.Market).all()
    return markets

# GET → Obter um mercado por ID
@router.get("/{market_id}", response_model=market_schema.Market)
def get_market(market_id: int, db: Session = Depends(get_db)):
    market = db.query(models.Market).filter(models.Market.id == market_id).first()
    if not market:
        raise HTTPException(status_code=404, detail="Market not found")
    return market

# POST → Criar um mercado
@router.post("/", response_model=market_schema.Market)
def create_market(market: market_schema.MarketCreate, db: Session = Depends(get_db)):
    db_market = models.Market(**market.dict())
    db.add(db_market)
    db.commit()
    db.refresh(db_market)
    return db_market

# PUT → Atualizar um mercado
@router.put("/{market_id}", response_model=market_schema.Market)
def update_market(market_id: int, market: market_schema.MarketCreate, db: Session = Depends(get_db)):
    db_market = db.query(models.Market).filter(models.Market.id == market_id).first()
    if not db_market:
        raise HTTPException(status_code=404, detail="Market not found")

    for key, value in market.dict().items():
        setattr(db_market, key, value)

    db.commit()
    db.refresh(db_market)
    return db_market

# DELETE → Deletar um mercado
@router.delete("/{market_id}")
def delete_market(market_id: int, db: Session = Depends(get_db)):
    db_market = db.query(models.Market).filter(models.Market.id == market_id).first()
    if not db_market:
        raise HTTPException(status_code=404, detail="Market not found")

    db.delete(db_market)
    db.commit()
    return {"detail": "Market deleted successfully"}
