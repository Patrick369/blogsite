from fastapi import FastAPI

from db import models
from db.database import engine
# from sqlalchemy.orm import Session
from routers import blogs

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(blogs.router)


#
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#

@app.get("/ping/{id}")
def say_hi(id: int):
    return {"message": "pong!" + str(id)}
#
# @app.post("/users", response_model=schema.User)
# def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
#     created_user = crud.get_user_by_email(db, email=user.email)
#     if created_user:
#         return HTTPException(status_code=400, detail="Email already registered.")
#     return crud.create_user(db, user=user)
