from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class ReceiptProductBase(BaseModel):
    product_id: int
    quantity: int
    unit_price: float
    total_price: float

class ReceiptProductCreate(ReceiptProductBase):
    pass

class ReceiptProduct(ReceiptProductBase):
    id: int

    class config:
        orm_mode = True

class ReceiptBase(BaseModel):
    user_id: int
    market_id: int
    total_amout: Optional[float] = None

class ReceiptCreate(ReceiptBase):
    products: List[ReceiptProductCreate]

class Receipt(ReceiptBase):
    id: int
    date: datetime
    products: List[ReceiptProduct] = []

    class Config:
        orm_mode = True