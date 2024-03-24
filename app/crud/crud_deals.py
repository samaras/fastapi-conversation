from sqlalchemy.orm import Session
from models.deal import Deal
from schemas.deal import DealCreate


def create_deal(
    db: Session, name: str, amount: int, stage: str, lead_id: int, customer_id: int
):
    db_deal = Deal(
        name=name, amount=amount, stage=stage, lead_id=lead_id, customer_id=customer_id
    )
    db.add(db_deal)
    db.commit()
    db.refresh(db_deal)
    return db_deal


def get_deal(db: Session, deal_id: int):
    return db.query(Deal).filter(Deal.id == deal_id).first()


def get_all_deals(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Deal).offset(skip).limit(limit).all()
