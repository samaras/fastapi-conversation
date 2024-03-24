from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas import user as user_schemas, email as email_schemas
from crud import crud_users as crud
from db.database import get_db

router = APIRouter()


@router.post("/users/", response_model=user_schemas.User)
def create_user(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # For demonstration purposes only, please hash your passwords
    return crud.create_user(
        db=db,
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        password=user.password,
    )


@router.get("/users/", response_model=list[user_schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_all_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=user_schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
