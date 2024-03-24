from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel, Field


class CampaignBase(BaseModel):
    name: str
    html_content: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    description: Optional[str] = None
    sendgrid_campaign_id: Optional[str] = None


class CampaignCreate(CampaignBase):
    pass


class Campaign(CampaignBase):
    id: int
    created_at: datetime = Field(default_factory=datetime.now)

    class Config:
        from_attributes = True
