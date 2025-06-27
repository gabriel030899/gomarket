from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    name: str
    brand: Optional[str] = None
    category: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class config:
        orm_mode = True