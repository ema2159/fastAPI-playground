from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.orm.query import Query

from . import models, schemas

# Create
def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    db_user = models.User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        address=user.address,
        phone_num=user.phone_num,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Read
def get_user(db: Session, user_id: int) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[models.User]:
    return db.query(models.User).offset(skip).limit(limit).all()
