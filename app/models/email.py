from sqlalchemy import Boolean, Column, DateTime, Integer, String, ForeignKey, func
from sqlalchemy.orm import relationship

from db.database import Base


class Email(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String)
    body = Column(String)
    sender = Column(String, nullable=False)
    recipient = Column(String, nullable=False)
    sendgrid_email_id = Column(String)
    sent_at = Column(DateTime, default=func.now())
    is_opened = Column(Boolean, default=False)
    lead_id = Column(Integer, ForeignKey("leads.id"))

    lead = relationship("Lead", back_populates="message")
