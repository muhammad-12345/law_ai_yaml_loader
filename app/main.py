from fastapi import FastAPI, Depends
from app.config import load_settings, Settings

app = FastAPI()

def get_settings() -> Settings:
    return load_settings()

@app.get("/settings")
def read_settings(settings: Settings = Depends(get_settings)):
    return settings.dict()
