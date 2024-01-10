from sqlalchemy import Boolean, Column, Integer, String, DateTime, func
from core.Database import Base
from core.Enum import Role


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String(255))
    email = Column(String(255), unique=True)
    username = Column(String(255), unique=True)
    password = Column(String(255))
    created_at = Column(DateTime, default=func.now())
    active = Column(Boolean, default=True)
    role = Column(String(20), default=Role.USER)
