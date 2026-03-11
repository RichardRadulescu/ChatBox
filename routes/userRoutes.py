from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from db.usersTable import UsersTable
from models.file import FileRead, FileWrite
from models.user import UserRead, UserWrite

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=List[UserRead])
def read_users(db: Session = Depends(get_db)):
    result = db.query(UsersTable).all()
    return result


@router.get("/{user_id}", response_model=UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UsersTable).filter(UsersTable.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/{user_id}/files", response_model=FileRead)
def create_user_file(user_id: int, file_data: FileWrite, db: Session = Depends(get_db)):
    pass
