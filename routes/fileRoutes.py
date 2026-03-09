from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.filesTable import FilesTable
from db.database import get_db
from models.file import FileWrite, FileRead


router = APIRouter(prefix="/files", tags=["files"])


@router.get("/", response_model=list[FileRead])
def read_files(db: Session = Depends(get_db)):
    return db.query(FilesTable).all()


@router.post("/user/{user_id}/create", response_model=FileRead)
def create_user_file(user_id: int, file_data: FileWrite, db: Session = Depends(get_db)):
    pass


@router.delete("/{file_id}")
def delete_file(file_id: int, db: Session = Depends(get_db)):
    db_file = db.query(FilesTable).filter(FilesTable.id == file_id).first()
    if not db_file:
        raise HTTPException(status_code=404, detail="File not found")
    db.delete(db_file)
    db.commit()
    return {"message": "Deleted"}
