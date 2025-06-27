from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import models, schemas
from app.database import Sessionlocal

router = APIRouter(
    prefix="/receipt",
    tags=["Receipts"]
)

# Dependência para obter a sessão do banco
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()


# GET → Listar todos os recibos
@router.get("/", response_model=List[schemas.receipt.Receipt])
def get_receipts(db: Session = Depends(get_db)):
    receipts = db.query(models.Receipt).all()
    return receipts

# GET → Obter recibo por ID
@router.get("/{receipt_id}", response_model=schemas.receipt.Receipt)
def get_receipt(receipt_id: int, db: Session = Depends(get_db)):
    receipt = db.query(models.Receipt).filter(models.Receipt.id == receipt_id).first()
    if not receipt:
        raise HTTPException(status_code=404, detail="Recibo não encontrado")
    return receipt

# POST → Criar um novo recibo
@router.post("/", response_model=schemas.receipt.Receipt)
def create_receipt(receipt: schemas.receipt.ReceiptCreate, db: Session = Depends(get_db)):
    db_receipt = models.Receipt(**receipt.dict())
    db.add(db_receipt)
    db.commit()
    db.refresh(db_receipt)
    return db_receipt

# PUT → Atualizar um recibo existente
@router.put("/{receipt_id}", response_model=schemas.receipt.Receipt)
def update_receipt(receipt_id: int, receipt: schemas.receipt.ReceiptUpdate, db: Session = Depends(get_db)):
    db_receipt = db.query(models.Receipt).filter(models.Receipt.id == receipt_id).first()
    if not db_receipt:
        raise HTTPException(status_code=404, detail="Recibo não encontrado")
    db.commit()
    db.refresh(db_receipt)
    return db_receipt

# DELETE → Excluir um recibo
@router.delete("/{receipt_id}", response_model=schemas.receipt.Receipt)
def delete_receipt(receipt_id: int, db: Session = Depends(get_db)):
    db_receipt = db.query(models.Receipt).filter(models.Receipt.id == receipt_id).first()
    if not db_receipt:
        raise HTTPException(status_code=404, detail="Recibo não encontrado")
    db.delete(db_receipt)
    db.commit()
    return {"detail": "Recibo excluído com sucesso"}

