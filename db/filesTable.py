from sqlalchemy import BLOB, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, relationship
from db.userFilesTable import user_file_link


class FilesTable(DeclarativeBase):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    textContent = Column(String)
    blobContent = Column(BLOB)
    files = relationship("FilesTable", secondary=user_file_link, back_populates="users")
