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
    @app.post("/api/analyze")
def analyze(data: TextInput):
    text = data.text.lower()
    if "stressed" in text or "tension" in text:
        emotion = "stressed"
        advice = "Take 3 deep breaths bro. You got this 💪"
    elif "sad" in text:
        emotion = "sad" 
        advice = "Talk to someone you trust. 1 day at a time."
    else:
        emotion = "okay"
        advice = "Keep going king"
    
    return {"emotion": emotion, "advice": advice}

@app.get("/")
def home():
    return {"message": "Fluente API is live"}
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel


app = FastAPI(title="Fluente Lite")

class TextInput(BaseModel):
    text: str

@app.post("/api/analyze-audio")
async def analyze_audio(file: UploadFile = File(...)):

    return {
        "transcript": "I recorded this with my voice",
        "confidence": 0.87,
        "clarity": 92
    }


@app.post("/api/analyze")
def analyze(data: TextInput):

    text = data.text.lower()

    if "stressed" in text or "tension" in text:
        emotion = "stressed"
        advice = "Take 3 deep breaths bro. You got this 💪"

    elif "sad" in text:
        emotion = "sad"
        advice = "Talk to someone you trust. 1 day at a time."

    elif "happy" in text or "good" in text:
        emotion = "happy"
        advice = "Keep going! You're doing great."

    else:
        emotion = "okay"
        advice = "Keep going king."


    return {
        "emotion": emotion,
        "advice": advice,
        "confidence": 0.85
    }

@app.get("/")
def home():

    return {
        "message": "Fluente API is live"
    }
