from fastapi import Depends, FastAPI, HTTPException
from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Users
@app.post("/users", tags=["userAPI"])
def post_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users", tags=["userAPI"])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip, limit)


@app.get("/users/{user_id}", tags=["userAPI"])
def get_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)


@app.delete("/users/{user_id}", tags=["userAPI"])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    if not crud.delete_user(db, user_id):
        raise HTTPException(status_code=404, detail="Could not delete. User not found")
    return {"ok": True}
