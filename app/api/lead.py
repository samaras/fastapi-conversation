from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas import lead as lead_schemas
from crud import crud_leads
from db.database import get_db

router = APIRouter()


@router.post("/leads/", response_model=lead_schemas.Lead)
def create_lead(lead: lead_schemas.LeadCreate, db: Session = Depends(get_db)):
    return crud_leads.create_lead(
        db=db, name=lead.name, phone=lead.phone, email=lead.email, status=lead.status
    )


@router.get("/leads/{lead_id}", response_model=lead_schemas.Lead)
def read_lead(lead_id: int, db: Session = Depends(get_db)):
    db_lead = crud_leads.get_lead(db=db, lead_id=lead_id)
    if db_lead is None:
        raise HTTPException(status_code=404, detail="Lead not found")
    return db_lead


@router.get("/leads/", response_model=List[lead_schemas.Lead])
def read_leads(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_leads.get_all_leads(db=db, skip=skip, limit=limit)
