from typing import List, Optional
from .item import ItemFromUser
from datetime import datetime

from pydantic import BaseModel

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str

class UserUpdate(UserCreate):
    updated_at : datetime = datetime.utcnow()

class User(UserBase):
    id: int
    is_active: bool
    items: List[ItemFromUser] = []
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True