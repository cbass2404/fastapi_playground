from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from . import crud, models, schemas, authentication
from .database import SessionLocal, engine, get_db
from .routers import user, todo, authentication as auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth.router)
app.include_router(todo.router)
app.include_router(user.router)
