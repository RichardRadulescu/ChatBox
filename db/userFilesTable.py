from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import DeclarativeBase


user_file_link = Table(
    "User_Files",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("Users.id"), primary_key=True),
    Column("file_id", Integer, ForeignKey("Files.id"), primary_key=True),
)
