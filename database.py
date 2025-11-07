from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()  # Loads .env file

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_USER_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# ✅ Correct Database URI (Note: '@' and correct driver name)
DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# ✅ Create Engine
engine = create_engine(DATABASE_URI)

# ✅ Create SessionLocal
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ Base Class for Models
Base = declarative_base()
