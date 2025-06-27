from pydantic import BaseModel

class MarketBase(BaseModel):
    name: str
    address: str
    city: str

class MarketCreate(MarketBase):
    pass

class MarketUpdate(MarketBase):
    pass

class Market(MarketBase):
    id: int

    class Config:
        orm_mode = True