from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import schema, crud
from db.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.get("/blogs", tags=['blogs'])
def get_blog_list():
    return {"Hello blogs page."}


@router.get("/{username}/blogs", tags=["blogs"])
def get_blog_by_author(username: str):
    return ['']


@router.post("/blogs/create", response_model=schema.Blog, tags=["blogs"])
async def create_blog(blog: schema.BlogCreate, db: Session = Depends(get_db)):
    created_blog = crud.get_blog_by_title(db, blog)
    if created_blog:
        return HTTPException(status_code=400, detail="Blog already existed.")
    return crud.create_blog(db, blog)
