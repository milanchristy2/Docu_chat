from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv 

load_dotenv()

DATABASE_URL=os.getenv("DATABASE_URL")
if not DATABASE_URL:
    DATABASE_URL="sqlite:///./rag.db"
engine=create_engine(DATABASE_URL,pool_pre_ping=True)
Session=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()