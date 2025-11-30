from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from agents.chat import simple_chat
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

@app.get("/")
def read_root():
    return {"Ai Chat-bot is running"}

@app.post("/chat")
def chat(request: ChatRequest):
    return {"response": simple_chat(request.message)}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
