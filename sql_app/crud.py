import random
from typing import Optional
from sqlalchemy.orm import Session

from . import models, schemas

# User
# Create
def random_user_id(db: Session):
    min = 0
    max = 9999_9999_9999_9999
    rand_id = random.randint(min, max)

    while (
        db.query(models.User).filter(models.User.id == rand_id).limit(1).first()
        is not None
    ):
        rand_id = random.randint(min, max)

    return rand_id


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    db_user = models.User(
        id=random_user_id(db),
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


# Delete
def delete_user(db: Session, user_id: int) -> int:
    users_found = db.query(models.User).filter(models.User.id == user_id).delete()
    db.commit()
    return users_found
