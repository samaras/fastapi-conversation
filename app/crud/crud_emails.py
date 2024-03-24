from sqlalchemy.orm import Session
from models.email import Email
from schemas.email import EmailCreate


def create_email(
    db: Session, subject: str, body: str, sender: str, recipient: str, lead_id: int
):
    db_email = Email(
        subject=subject,
        body=body,
        sender=sender,
        recipient=recipient,
        lead_id=lead_id,
    )
    db.add(db_email)
    db.commit()
    db.refresh(db_email)
    return db_email


def get_email(db: Session, email_id: int):
    return db.query(Email).filter(Email.id == email_id).first()


def get_all_emails(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Email).offset(skip).limit(limit).all()
