from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..dependencies import get_db
from .. import models, schemas

router = APIRouter(
    prefix="/items",
    tags=["items"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=schemas.Item)
async def read_items(db : Session = Depends(get_db)):
    items = db.query(models.Item).all()
    return items

@router.put("/{item_id}")
async def update_item(item_id: int, item_input: schemas.ItemUpdate, db: Session= Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    item.title = item_input.title
    item.description = item_input.description
    item.updated_at = item_input.updated_at
    db.commit()
    db.refresh(item)
    return item