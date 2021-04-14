from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_400_BAD_REQUEST
from . import models, schemas
from app.authentication import Hash


# TO DO
def create_todo(db: Session, todo: schemas.TodoBase, user_id: int):
    new_todo = models.Todo(**todo.dict(), owner_id=user_id)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


def complete_todo(db: Session, todo_id: int, user_id: int):
    db_todo = db.query(models.Todo).filter(
        models.Todo.owner_id == user_id and models.Todo.id == todo_id).first()
    if db_todo:
        db_todo.complete = True
        db.commit()
        db.refresh(db_todo)
        return db_todo
    else:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail=f"Something Went Wrong")


def delete_todo(db: Session, todo_id: int, user_id: int):
    db_todo = db.query(models.Todo).filter(
        models.Todo.owner_id == user_id and models.Todo.id == todo_id).first()
    if db_todo:
        db.delete(db_todo)
        db.commit()
        return "Deleted Successfully"
    else:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail=f"Something Went Wrong")


# USER
def create_user(db: Session, user: schemas.UserCreate):
    db_user = db.query(
        models.User).filter(models.User.username == user.username).first()
    if db_user is None:
        new_user = models.User(username=user.username,
                               hashed_password=Hash.hash_password(
                                   user.password))
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                        detail=f"Username Taken")


def get_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        return db_user
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="User Not Found")


# UPDATE USER
# TODO

# DELETE USER
# TODO
