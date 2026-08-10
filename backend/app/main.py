from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from .routers import audio  
app = FastAPI(
    title="Fluento API",
    description="AI Speaking Coach Backend",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Fluento Backend is LIVE 🚀"}

@app.get("/health")
def health():
    return {"status": "ok", "db": "connected"}

from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str
    language: str = "en"

@app.post("/api/analyze")
def analyze_text(req: TextRequest):
    # simple emotion detection for now
    emotion = "neutral"
    if "sad" in req.text.lower(): emotion = "sad"
    if "anxious" in req.text.lower() or "stress" in req.text.lower(): emotion = "anxious"
    if "happy" in req.text.lower() or "great" in req.text.lower(): emotion = "happy"
    
    return {
        "emotion": emotion,
        "confidence": 0.85,
        "advice": "Take a deep breath. You got this 💙",
        "text_received": req.text
    }
