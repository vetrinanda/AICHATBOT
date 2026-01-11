from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from agents.chat import simple_chat
from agents.rag import rag_chat
from agents.youtube_rag import extract_video_information
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    
class InfoRequest(BaseModel):
    input_url:str
    question:str

class RAGRequest(BaseModel):
    documents: str
    query: str


@app.get("/")
def read_root():
    return {"Ai Chat-bot is running"}

@app.post("/chat")
def chat(request: ChatRequest):
    return {"response": simple_chat(request.message)}


@app.post("/rag")
def rag(request: RAGRequest):
    return {"response": rag_chat(request.documents, request.query)}

@app.post("/youtube_rag")
def youtube_rag(request: InfoRequest):
    return {"response": extract_video_information(request.input_url, request.question)}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
