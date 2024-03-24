from sqlalchemy import Column, DateTime, Integer, String, func
from sqlalchemy.orm import relationship

from db.database import Base


class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(60), index=True, nullable=False)
    email = Column(String, index=True)
    phone = Column(String)
    status = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())

    deal = relationship("Deal", back_populates="lead")
    message = relationship("Email", back_populates="lead")
