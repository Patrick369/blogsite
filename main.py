from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from db import crud, models, schema
from db.database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/ping/{id}")
def say_hi(id: int):
    return {"message": "pong!" + str(id)}


@app.post("/users", response_model=schema.User)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    created_user = crud.get_user_by_email(db, email=user.email)
    if created_user:
        return HTTPException(status_code=400, detail="Email already registered.")
    return crud.create_user(db, user=user)
