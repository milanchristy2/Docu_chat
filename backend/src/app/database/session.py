from backend.src.app.core.config import Session

def get_db():
    db=Session()
    try:
        yield db
    finally:
        db.close()
