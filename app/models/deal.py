from sqlalchemy import Column, DECIMAL, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db.database import Base


class Deal(Base):
    __tablename__ = "deals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    amount = Column(DECIMAL(10, 2))
    stage = Column(String)
    lead_id = Column(Integer, ForeignKey("leads.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))

    lead = relationship("Lead", back_populates="deal")
    customer = relationship("Customer", back_populates="deal")
