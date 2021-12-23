from datetime import datetime
from typing import List, Optional, Text

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True


# Blog CreateRequest Object

class BlogCreate(BaseModel):
    title: str
    content: Text
    author_id: int
    pub_date: datetime = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
    mod_date: datetime = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")

    class Config:
        orm_mode = True
