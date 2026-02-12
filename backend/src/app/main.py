import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.src.app.api.routes.router import router
import uvicorn

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router)

def start():
    uvicorn.run("backend.src.app.main:app",host="127.0.0.1",port=8000,reload=True)

if __name__=="__main__":
    start()

