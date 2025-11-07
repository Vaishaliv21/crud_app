from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import Base
from database import engine, SessionLocal

app = FastAPI(title="CRUD APPLICATION")

# Create tables once during startup
@app.on_event("startup")
def start_up():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "FastAPI CRUD is running successfully!"}


# ✅ Corrected DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
