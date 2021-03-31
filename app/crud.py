from sqlalchemy.orm import Session
from . import models, schemas


def create_todo(db: Session, todo: schemas.TodoBase):
    new_todo = models.Todo(**todo.dict())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


def create_user(db: Session, user: schemas.UserCreate):
    new_user = models.User()
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user