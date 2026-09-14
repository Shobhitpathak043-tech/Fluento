from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

app = FastAPI(title="Fluente Lite")


class TextInput(BaseModel):
    text: str


@app.post("/api/analyze-audio")
async def analyze_audio(file: UploadFile = File(...)):

    try:
    
        audio_data = await file.read()

        print("Audio received:", file.filename)
        print("Content type:", file.content_type)
        print("Audio size:", len(audio_data), "bytes")

        if len(audio_data) == 0:
            return {
                "error": "The audio file is empty."
            }

    
        return {
            "transcript": "I recorded this with my voice",
            "confidence": 87,
            "clarity": 92
        }

    except Exception as e:

        print("AUDIO ERROR:", str(e))

        return {
            "error": str(e)
        }

@app.post("/api/analyze")
def get_emotion(text):
    text = text.lower()
    if "sad" in text or "depressed" in text or "lonely" in text:
        return "sad"
    elif "angry" in text or "mad" in text or "frustrated" in text:
        return "angry"
    elif "stress" in text or "anxiety" in text or "tensed" in text:
        return "stressed"
    elif "happy" in text or "good" in text or "great" in text:
        return "happy"
    else:
        return "neutral"

def get_advice(emotion):
    if emotion == "sad":
        return "It's okay to feel sad. Talk to a friend you trust and write down 1 good thing that happened today 💙"
    elif emotion == "angry":
        return "Anger is valid. Take 10 deep breaths, go for a 5 min walk, don't reply right now."
    elif emotion == "stressed":
        return "Stress is heavy. Make 1 page notes, do 3 deep breaths, tackle one small task."
    elif emotion == "happy":
        return "Love that energy! Save this feeling, share it with someone today."
    else:
        return "Thanks for sharing. Take a deep breath, you got this 💙"

@app.get("/")
def home():

    return {
        "message": "Fluente API is live"
    }
