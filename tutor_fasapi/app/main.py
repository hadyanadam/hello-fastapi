from fastapi import Depends, FastAPI

from .dependencies import oauth2_scheme
from .internal import admin
from .routers import items, users
from .db import SessionLocal, engine, Base
# from . import models


app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    # dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)

Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

@app.get("/token")
async def get_token(token:str = Depends(oauth2_scheme)):
    return {"token" : token}