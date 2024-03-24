from sqlalchemy import Column, DateTime, Integer, String, func
from sqlalchemy.orm import relationship

from db.database import Base


class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    html_content = Column(String)
    sendgrid_campaign_id = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    description = Column(String)
