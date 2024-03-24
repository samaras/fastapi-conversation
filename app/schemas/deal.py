from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field


class DealBase(BaseModel):
    name: str
    amount: Optional[float] = None
    stage: Optional[str] = None
    lead_id: Optional[int] = None
    customer_id: Optional[int] = None


class DealCreate(DealBase):
    pass


class Deal(DealBase):
    id: int
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    class Config:
        from_attributes = True
