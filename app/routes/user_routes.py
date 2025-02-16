from fastapi import APIRouter, HTTPException
from app.db import db
from app.models import User

router = APIRouter()

@router.post("/register")
def register_user(user: User):
    if db.users.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    db.users.insert_one(user.dict())
    return {"message": "User registered successfully"}

@router.get("/")
def get_users():
    return list(db.users.find({}, {"_id": 0, "password": 0}))
