from typing import List, Optional

from datetime import datetime
from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemCreate):
    updated_at: datetime = datetime.utcnow()


class ItemFromUser(ItemBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True