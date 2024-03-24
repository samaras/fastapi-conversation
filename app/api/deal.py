from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas import deal as deal_schemas
from crud import crud_deals
from db.database import get_db

router = APIRouter()


@router.post("/deals/", response_model=deal_schemas.Deal)
def create_deal(deal: deal_schemas.DealCreate, db: Session = Depends(get_db)):
    return crud_deals.create_deal(db=db, **deal.dict())


@router.get("/deals/{deal_id}", response_model=deal_schemas.Deal)
def read_deal(deal_id: int, db: Session = Depends(get_db)):
    db_deal = crud_deals.get_deal(db=db, deal_id=deal_id)
    if db_deal is None:
        raise HTTPException(status_code=404, detail="Deal not found")
    return db_deal


@router.get("/deals/", response_model=List[deal_schemas.Deal])
def read_deals(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_deals.get_all_deals(db=db, skip=skip, limit=limit)
