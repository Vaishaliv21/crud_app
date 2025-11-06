from sqlalchemy import *
from fastapi import *
import os
from dotenv import load_dotenv
load_dotenv() # load enviornment variations 
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_USER_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_POST = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


app = FastAPI(title="CRUD APPLICATION")
DATABASE_DB = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_POST}/{DB_NAME}"

engine = create_engine(DATABASE_DB)
@app.get("/")
def root():
    return {"message": "FastAPI CRUD is running successfully!"}

@app.post("/add_user")
def add_user(name: str, email: str, db=Depends(get_db)):
    new_user = Users(name=name, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User added successfully!"}


# ✅ Get All Users API
@app.get("/users")
def get_users(db=Depends(get_db)):
    users = db.query(Users).all()
    return users 
