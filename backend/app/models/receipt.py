from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float, func
from sqlalchemy.orm import relationship
from app.database import Base

class Receipt(Base):
    __tablename__ = "receipts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    market_id = Column(Integer, ForeignKey("markets.id"), nullable=False)
    date = Column(DateTime, default=func.now())
    total_amount = Column(Float, nullable=True)

    # Relacionamentos
    user = relationship("User")
    market = relationship("Market")
    products = relationship("ReceiptProduct", back_populates="receipt")

class ReceiptProduct(Base):
    __tablename__ = "receipt_products"

    id = Column(Integer, primary_key=True, index=True)
    receipt_id = Column(Integer, ForeignKey("receipts.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    total_price = Column(Float, nullable=False)

    # Relacionamentos
    receipt = relationship("Receipt", back_populates="products")
    product = relationship("Product")