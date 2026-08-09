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
