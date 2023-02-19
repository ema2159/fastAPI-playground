from sqlalchemy.orm import Session
from sqlalchemy.orm.query import Query

from . import models, schemas


def get_user(db: Session, user_id: int) -> Query[models.User]:
    return db.query(models.User).filter(models.User.id == user_id).first()


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
