from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate


def create_user(db: Session, username: str, email: str, full_name: str, password: str):
    db_user = User(
        username=username,
        email=email,
        full_name=full_name,
        password=password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    user = db.query(User).filter(User.email == email).first()
    return user


def get_all_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()
