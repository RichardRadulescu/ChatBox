from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import DeclarativeBase


user_file_link = Table(
    "user_file_link",
    DeclarativeBase.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("file_id", Integer, ForeignKey("files.id"), primary_key=True),
)
