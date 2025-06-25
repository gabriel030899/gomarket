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
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return product

# POST → Criar um novo produto
@router.post("/", response_model=schemas.product.Product)
def create_product(product: schemas.product.ProductCreate, db: Session = Depends(get_db)):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# PUT → Atualizar um produto existente
@router.put("/{product_id}", response_model=schemas.product.Product)
def update_product(product_id: int, product: schemas.product.ProductUpdate, db: Session = Depends(get_db)):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    for key, value in product.dict().items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)
    return db_product

# DELETE → Excluir um produto
@router.delete("/{product_id}", response_model=schemas.product.Product)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    db.delete(db_product)
    db.commit()
    return {"detail": "Produto excluído com sucesso"}