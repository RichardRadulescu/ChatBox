import io
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import PlainTextResponse, StreamingResponse
from sqlalchemy.orm import Session

from db.database import get_db
from db.filesTable import FilesTable
from db.usersTable import UsersTable
from models.file import FileRead, FileWrite
from models.user import UserRead
from utils.security import get_current_user

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


@router.post("/me/files", response_model=FileRead)
def create_user_file(
    file_data: FileWrite,
    user: UserRead = Depends(get_current_user),
    db: Session = Depends(get_db),
):

    db_file = FilesTable(  # noqa: F821
        name=file_data.name,
        type=file_data.type,
        text_content=file_data.text_content,
        blob_content=file_data.blob_content,
        owners=[user],  # This is the "magic" link
    )

    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file


@router.get("/me/files/{file_id}", response_model=FileRead)
def get_user_file(
    file_id: int,
    user: UserRead = Depends(get_current_user),
    db: Session = Depends(get_db),
):

    file = (
        db.query(FilesTable)
        .join(FilesTable.owners)
        .filter(FilesTable.id == file_id, UsersTable.id == user.id)
        .first()
    )

    if not file:
        raise HTTPException(status_code=404, detail="File not found or not yours")

    return file


@router.get("/me/files/{file_id}/download")
def download_file(
    file_id: int,
    user: UserRead = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    file = (
        db.query(FilesTable)
        .join(FilesTable.owners)
        .filter(FilesTable.id == file_id, UsersTable.id == user.id)
        .first()
    )

    if not file:
        raise HTTPException(status_code=404, detail="File not found")

    # Return text content if present
    if file.text_content is not None:
        return PlainTextResponse(
            content=file.text_content,
            media_type=file.type,
            headers={"Content-Disposition": f'attachment; filename="{file.name}"'},
        )

    # Return binary content if present
    if file.blob_content is not None:
        return StreamingResponse(
            io.BytesIO(file.blob_content),
            media_type=file.type,
            headers={"Content-Disposition": f'attachment; filename="{file.name}"'},
        )

    raise HTTPException(status_code=400, detail="File has no content")
