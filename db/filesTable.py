from sqlalchemy import BLOB, Column, Integer, String
from sqlalchemy.orm import relationship

from db.database import Base, user_file_link


class FilesTable(Base):
    __tablename__ = "Files"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    text_content = Column("textContent", String)
    blob_content = Column("blobContent", BLOB)
    owners = relationship(
        "UsersTable", secondary=user_file_link, back_populates="files"
    )
