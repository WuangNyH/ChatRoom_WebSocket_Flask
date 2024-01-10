from sqlalchemy import Boolean, Column, Integer, String, DateTime, func
from core.Database import Base


class Message(Base):
    __tablename__ = 'messengers'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code_room = Column(String(20), nullable=False)
    content = Column(String(500), nullable=False)
    username = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=func.now())
