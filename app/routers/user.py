from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud, authentication
from app.database import get_db

router = APIRouter()


@router.post("/create_user", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user=user)


@router.get("/get_user/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id=user_id)


# @router.post("/update_user")
# def update_user(current_user: schemas.User = Depends(
#     authentication.get_current_user),
#                 db: Session = Depends(get_db)):
#     return crud.update_user(db, user_id=current_user.id)


@router.delete("/delete_user")
def delete_user(current_user: schemas.User = Depends(
    authentication.get_current_user),
                db: Session = Depends(get_db)):
    return crud.delete_user(db, user_id=current_user.id)
