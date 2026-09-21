from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

app = FastAPI(title="Fluente Lite")

class TextInput(BaseModel):
    text: str

def get_emotion(text: str):
    text = text.lower()
    if "sad" in text or "depressed" in text or "lonely" in text:
        return "sad"
    elif "angry" in text or "mad" in text or "frustrated" in text:
        return "angry"
    elif "stress" in text or "anxiety" in text or "tense" in text:
        return "stressed"
    elif "happy" in text or "good" in text or "great" in text:
        return "happy"
    else:
        return "neutral"

def get_advice(emotion: str):
    if emotion == "sad":
        return "It's okay to feel sad. Talk to a friend you trust and rest."
    elif emotion == "angry":
        return "Anger is valid. Take 10 deep breaths, go for a 5 min walk."
    elif emotion == "stressed":
        return "Stress is heavy. Make 1 page notes, do 3 deep breaths, drink water."
    elif emotion == "happy":
        return "Love that energy! Save this feeling, share it with someone."
    else:
        return "Thanks for sharing. Take a deep breath, you got this."

@app.post("/api/analyze-audio")
async def analyze_audio(file: UploadFile = File(...)):
    try:
        audio_data = await file.read()
        if len(audio_data) == 0:
            return {"error": "The audio file is empty."}
        
    
        emotion = "stressed"  
        return {
            "emotion": emotion,
            "feeling": emotion,
            "advice": get_advice(emotion),
            "confidence": 87,
            "clarity": 92,
            "transcript": "I recorded this with my voice"
        }
    except Exception as e:
        return {"error": str(e)}

@app.post("/api/analyze")
def analyze_text(input: TextInput):
    emotion = get_emotion(input.text)
    return {
        "emotion": emotion,
        "advice": get_advice(emotion),
        "confidence": 85
    }

@app.get("/")
def home():
    return {"message": "Fluente API is live"}
