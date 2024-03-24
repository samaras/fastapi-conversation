from datetime import datetime
from sqlalchemy.orm import Session
from models.campaign import Campaign
from schemas.campaign import CampaignCreate


def add_campaign(
    db: Session,
    name: str,
    html_content: str,
    sendgrid_campaign_id: str,
    start_date: datetime,
    end_date: datetime,
    description: str,
):
    db_campaign = Campaign(
        name=name,
        html_content=html_content,
        sendgrid_campaign_id=sendgrid_campaign_id,
        start_date=start_date,
        end_date=end_date,
        description=description,
    )
    db.add(db_campaign)
    db.commit()
    db.refresh(db_campaign)
    return db_campaign


def get_campaign(db: Session, campaign_id: int):
    return db.query(Campaign).filter(Campaign.id == campaign_id).first()


def get_all_campaigns(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Campaign).offset(skip).limit(limit).all()
