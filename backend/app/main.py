from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import predictions, admin, stats
from .ml_model import train_model
import os

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

app.include_router(predictions.router)
app.include_router(admin.router)
app.include_router(stats.router)

@app.on_event("startup")
def startup_event():
    if not os.path.exists("backend/data/trained_model.pkl"):
        train_model()

@app.get("/")
def read_root(): return {"message": "PrevenTech API running"}