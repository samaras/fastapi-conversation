from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas import campaign as campaign_schemas
from crud import crud_campaigns
from db.database import get_db

router = APIRouter()


@router.post("/campaigns/", response_model=campaign_schemas.Campaign)
def create_campaign(
    campaign: campaign_schemas.CampaignCreate, db: Session = Depends(get_db)
):
    return crud_campaigns.add_campaign(db=db, **campaign.model_dump())


@router.get("/campaigns/{campaign_id}", response_model=campaign_schemas.Campaign)
def read_campaign(campaign_id: int, db: Session = Depends(get_db)):
    db_campaign = crud_campaigns.get_campaign(db=db, campaign_id=campaign_id)
    if db_campaign is None:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return db_campaign


@router.get("/campaigns/", response_model=List[campaign_schemas.Campaign])
def read_campaigns(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_campaigns.get_all_campaigns(db=db, skip=skip, limit=limit)
