from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr


class EmailBase(BaseModel):
    subject: Optional[str] = None
    body: Optional[str] = None
    sender: EmailStr
    recipient: EmailStr
    sendgrid_email_id: Optional[str] = None
    sent_at: Optional[datetime] = None
    is_opened: Optional[bool] = False
    lead_id: Optional[int] = None


class EmailCreate(EmailBase):
    pass


class Email(EmailBase):
    id: int

    class Config:
        from_attributes = True
