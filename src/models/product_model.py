from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.db.database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    reference = Column(String, index=True)
    type = Column(String, unique=True, index=True)
    status = Column(String)

    purchases = relationship("Purchases", back_populates="product")
