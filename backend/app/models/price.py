from sqlalchemy import Column, Integer, String, ForeignKey, func, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class Price(Base):
    __tablename__ = "prices"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    market_id = Column(Integer, ForeignKey("markets.id"), nullable = False)
    price = Column(Integer, nullable=False)
    date = Column(DateTime(timezone=True), server_default=func.now())

    # Relacionamentos
    product = relationship("Product")
    market = relationship("Market")