from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, relationship
from db.userFilesTable import user_file_link


class UsersTable(DeclarativeBase):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    users = relationship("UserTable", secondary=user_file_link, back_populates="files")
