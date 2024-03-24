from sqlalchemy import Column, DateTime, Integer, String, func
from sqlalchemy.orm import relationship

from db.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    email = Column(String, index=True)
    phone = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())

    deal = relationship("Deal", back_populates="customer")
