import bcrypt
from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from ..db import SessionLocal
from .. import models, schemas
# from sqlalchemy.orm import select
from ..dependencies import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}}
    )


@router.get("/", response_model=List[schemas.User])
async def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@router.post("/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    created_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(created_user)
    db.commit()
    db.refresh(created_user)
    return created_user

@router.get("/{user_id}", response_model=schemas.User)
async def get_user(user_id : int,db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    return user

@router.delete("/{user_id}", response_model=schemas.User)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(user)
    db.commit()
    return user

@router.put('/{user_id}', response_model=schemas.User)
async def update_user(user_id: int, user_input: schemas.UserUpdate, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    user.email = user_input.email
    user.updated_at = user_input.updated_at
    db.commit()
    db.refresh(user)
    return user

@router.post("/{user_id}/items", response_model=schemas.Item)
async def create_item(user_id: int, item_input: schemas.ItemCreate, db : Session = Depends(get_db)):
    item = models.Item(title=item_input.title, description=item_input.description, owner_id=user_id)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.get("/{user_id}/items", response_model=List[schemas.ItemFromUser])
async def get_items_user(user_id: int, db: Session = Depends(get_db)):
    user_items = db.query(models.Item).filter(models.Item.owner_id == user_id).all()
    return user_items