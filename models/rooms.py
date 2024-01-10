from sqlalchemy import Boolean, Column, Integer, String, DateTime, func
from core.Database import Base


class Room(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    room_name = Column(String(255))
    code_room = Column(String(20), unique=True, nullable=False)
    created_at = Column(DateTime, default=func.now())
    created_by = Column(String(255))
