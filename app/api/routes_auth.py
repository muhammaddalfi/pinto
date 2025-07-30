from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.services.auth_service import authenticate_user, login_user, register_user
from app.db.database import get_db

router = APIRouter(tags=["auth"])

@router.post("/auth/register")
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, user_in)

@router.post("/auth/login")
def login(user_in: UserCreate, db: Session = Depends(get_db)):
    user = authenticate_user(db, user_in.username, user_in.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"access_token": login_user(user), "token_type": "bearer"}
