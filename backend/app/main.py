from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

app = FastAPI(title="Fluente Lite")

class TextInput(BaseModel):
    text: str
    @app.post("/api/analyze-audio")
async def analyze_audio(file: UploadFile = File(...)):
    return {
        "transcript": "I recorded this with my voice", 
        "confidence": 87,
        "clarity": 92
    }

@app.get("/")
def home():
    return {"message": "Fluente API is live"}
