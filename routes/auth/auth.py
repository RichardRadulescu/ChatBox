from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.database import get_db
from db.usersTable import UsersTable
from models.user import UserRead, UserResponseWithToken, UserWrite
from utils.hashing import hash_password
from utils.security import create_access_token

router = APIRouter(prefix="/auth", tags=["users"])


async def verify_email_unique(user: UserWrite, db: Session = Depends(get_db)):
    userExists = db.query(UsersTable).filter(UsersTable.email == user.email).first()

    if userExists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered"
        )
    return userExists


@router.post("/", response_model=UserResponseWithToken)
def create_user(
    user: UserWrite,
    db: Session = Depends(get_db),
    _email_check=Depends(verify_email_unique),
):
    db_user = UsersTable(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        hashed_password=hash_password(user.password),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    data = {"sub": str(db_user.id)}
    token = create_access_token(data)

    return {"access_token": token, "token_type": "bearer", "user": db_user}
