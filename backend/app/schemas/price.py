from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PriceBase(BaseModel):
    market_id: int
    product_id: int
    price: float

class PriceCreated(PriceBase):
    pass

class Price(PriceBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True