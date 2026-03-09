from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from db.usersTable import UsersTable
from models.user import UserRead, UserWrite

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserRead)
def create_user(user: UserWrite, db: Session = Depends(get_db)):
    db_user = UsersTable(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        hashed_password=user.password + "notsecurehash",  # Hash this properly later!
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/{user_id}", response_model=UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UsersTable).filter(UsersTable.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
