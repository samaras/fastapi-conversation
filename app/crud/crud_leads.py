from sqlalchemy.orm import Session
from models.lead import Lead
from schemas.lead import LeadCreate


def create_lead(db: Session, name: str, email: str, phone: str, status: str):
    db_lead = Lead(name=name, email=email, phone=phone, status=status)
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    return db_lead


def get_lead(db: Session, lead_id: int):
    return db.query(Lead).filter(Lead.id == lead_id).first()


def get_all_leads(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Lead).offset(skip).limit(limit).all()
