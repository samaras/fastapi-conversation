from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas import customer as customer_schemas
from crud import crud_customers
from db.database import get_db

router = APIRouter()


@router.post("/customers/", response_model=customer_schemas.Customer)
def create_customer(
    customer: customer_schemas.CustomerCreate, db: Session = Depends(get_db)
):
    db_cust = crud_customers.get_customer_by_email(db, email=customer.email)
    if db_cust:
        raise HTTPException(
            status_code=400, detail="Customer with that email already exists!"
        )
    return crud_customers.add_customer(
        db=db, name=customer.name, email=customer.email, phone=customer.phone
    )


@router.get("/customers/{customer_id}", response_model=customer_schemas.Customer)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = crud_customers.get_customer(db=db, customer_id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer


@router.get("/customers/", response_model=List[customer_schemas.Customer])
def read_customers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_customers.get_all_customers(db=db, skip=skip, limit=limit)
