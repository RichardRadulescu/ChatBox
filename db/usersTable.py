from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base, user_file_link


class UsersTable(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column("firstName", String, nullable=False)
    last_name = Column("lastName", String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column("hashedPassword", String, nullable=False)
    files = relationship(
        "FilesTable", secondary=user_file_link, back_populates="owners"
    )
