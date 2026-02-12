import os
from pathlib import Path

BASE_DIR=Path(__file__).parent
UPLOAD_DIR=BASE_DIR/"uploads"
UPLOAD_DIR.mkdir(exist_ok=True)

def save_docs(filename:str,file_bytes:bytes)->str:
    path=UPLOAD_DIR/filename

    with open(path,"wb") as f:
        f.write(file_bytes)

    return str(path)