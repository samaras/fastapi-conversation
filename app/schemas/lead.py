from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr


class LeadBase(BaseModel):
    name: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    status: Optional[str] = None


class LeadCreate(LeadBase):
    pass


class Lead(LeadBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
