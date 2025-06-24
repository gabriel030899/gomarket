from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import models, schemas
from app.database import Sessionlocal

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

# Dependência para obter a sessão do banco
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

# GET → Listar todos os produtos
@router.get("/", response_model=List[schemas.product.Product])
def get_products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products

# GET → Obter produto por ID
@router.get("/{product_id}", response_model=schemas.product.Product)
def get_product(product_id: int, db: Session = Depends(get_db)):
    db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return product