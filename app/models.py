from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class ChatHistory(Base):
    __tablename__ = "chat_history"
    id: int = Column(Integer, primary_key=True, index=True)
    session_id: str = Column(String, index=True)
    user_message: str = Column(Text, nullable=False)
    bot_response: str = Column(Text, nullable=False)