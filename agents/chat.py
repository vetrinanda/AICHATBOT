from langchain_litellm import ChatLiteLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
import os
from dotenv import load_dotenv
from sqlalchemy import Session
import app.models as models
from app.database import SessionLocal, engine,Base
from uuid import UUID
from pydantic import BaseModel


class ChatSession(BaseModel):
    session_id: UUID
    user_message: str 
    bot_response: str  
    
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


load_dotenv()     

llm = ChatLiteLLM(
    api_key=os.getenv("API_KEY"),
    model=os.getenv("MODEL_NAME"),
    temperature=float(os.getenv("TEMPERATURE", "0.7"))
)

store = {}
def get_history(session_id: str) -> ChatMessageHistory:
    session_id=ChatSession.session_id
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

prompt = ChatPromptTemplate(messages=[
    ("system", "You are very  helpful and intelligent assistant."),
    ("placeholder", "{chat_history}"),
    ("human", "{user_input}"),
])

chain = prompt | llm

chat_memory = RunnableWithMessageHistory(
    runnable=chain,
    get_session_history=get_history,
    input_messages_key="user_input",
    history_messages_key="chat_history"
)

def simple_chat(user_input):
    response = chat_memory.invoke(
        {"user_input": user_input},

        {"configurable": {"session_id": "abc123"}}
    )   
    return response.content
