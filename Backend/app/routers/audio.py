from fastapi import APIRouter

router = APIRouter()

@router.post("/analyze")
async def analyze_audio():
    return {
        "status": "success",
        "fluency_score": 7.5,
        "feedback": "Good job! Try to speak slower and use more filler words."
    }
