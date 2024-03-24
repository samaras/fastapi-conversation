import os
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas import email as email_schemas
from crud import crud_emails
from db.database import get_db
from services.email_service import EmailService
from settings import settings


router = APIRouter()
api_key = settings.sendgrid_api_key


@router.post("/emails/", response_model=email_schemas.Email)
def send_email(email: email_schemas.EmailCreate, db: Session = Depends(get_db)):
    return EmailService.send_email(api_key=api_key, email_data=email, db=db)


@router.post("/emails/{email_id}/track-open")
def track_email_open(sendgrid_email_id: str, db: Session = Depends(get_db)):
    EmailService.track_email_open(sendgrid_email_id=sendgrid_email_id, db=db)
    return {"message": "Email open tracked successfully"}


@router.get("/emails/{email_id}/open-status", response_model=dict)
def get_email_open_status(email_id: int, db: Session = Depends(get_db)):
    return EmailService.get_email_open_status(email_id=email_id, db=db)
