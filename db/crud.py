from sqlalchemy.orm import Session

from . import models, schema


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schema.UserCreate):
    fake_hashed_password = user.password + "not_really_hashed"
    created_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(created_user)
    db.commit()
    db.flush(created_user)
    return created_user


###########Blog CRUD########################
def create_blog(db: Session, blog: schema.BlogCreate):
    """
    create blog of a author

    :param db:
    :param blog:
    :return:
    """
    blog = models.Blog(title=blog.title, content=blog.content, pub_date=blog.pub_date, mod_date=blog.mod_date,
                       author_id=blog.author_id)
    db.add(blog)
    db.commit()
    db.flush(blog)
    return blog
