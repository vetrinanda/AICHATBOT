import asyncio
import sys
from pathlib import Path

# Add parent directory to path so we can import app module
sys.path.insert(0, str(Path(__file__).parent.parent))



from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.models import ChatBot
from app.database import SessionLocal,engine,Base
from sqlalchemy.orm import Session
from pydantic_ai import Agent,VideoUrl
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider
import os
from dotenv import load_dotenv
load_dotenv()


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

class Message(BaseModel):
    user: str
    
class VideoInput(BaseModel):
    url: str
    question: str

ChatBot.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# db: Session = Depends(get_db)

provider = GoogleProvider(api_key=os.getenv("API_KEY"))
model = GoogleModel('gemini-3-flash-preview', provider=provider)
agent = Agent(model)

@app.post("/chatbot/")
async def create_chatbot(message: Message, db: Session = Depends(get_db)):
    response = await chatbot_agent(message.user)
    db_chatbot = ChatBot(user=message.user, airesponse=response)
    db.add(db_chatbot)
    db.commit()
    db.refresh(db_chatbot)
    return response


@app.post("/process-videourl/")
async def process_videourl(video: VideoInput):
    response = await video_url_agent(video.url, video.question)
    return response


async def chatbot_agent(question: str):
    response_text = ""
    async with agent.run_stream(question) as result:  
        async for message in result.stream_text():  
            response_text += message
    
    # Remove duplicate paragraphs from response
    response_text = remove_duplicate_paragraphs(response_text)
    return response_text.strip()


async def video_url_agent(url: str, text: str) -> str:
    result = await agent.run(
        [
            text,
            VideoUrl(url=url),
        ]
    )
    return result.output
    

def remove_duplicate_paragraphs(text: str) -> str:
    """Remove repeated paragraphs/sections from text"""
    lines = text.split('\n')
    seen = set()
    unique_lines = []
    
    for line in lines:
        line_stripped = line.strip()
        if line_stripped:
            # Check first 80 chars to detect repeated content
            line_sig = line_stripped[:80]
            if line_sig not in seen:
                seen.add(line_sig)
                unique_lines.append(line)
        elif unique_lines and unique_lines[-1].strip():
            # Keep one blank line between paragraphs
            unique_lines.append(line)
    
    return '\n'.join(unique_lines)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("bot:app", host="localhost", port=8000,reload=True)