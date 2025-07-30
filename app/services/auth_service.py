from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.db.models.user import User
from app.core.security import hash_password, verify_password, create_access_token
from app.schemas.user import UserCreate


def register_user(db: Session, user_in: UserCreate):
    existing = db.query(User).filter(User.username == user_in.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_pw = hash_password(user_in.password)
    user = User(username=user_in.username, hashed_password=hashed_pw)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"msg": "User registered successfully"}


def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user


def login_user(user: User):
    # Ambil daftar role dan permission dari relasi ORM
    roles = [role.name for role in user.roles]
    permissions = [perm.name for perm in user.permissions]

    token_data = {
        "sub": user.username,
        "roles": roles,
        "permissions": permissions
    }

    return create_access_token(token_data)
