from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.user_service import assign_role_to_user, assign_permission_to_user
from app.db.models.user import User

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/assign-role")
def assign_role(username: str, role_name: str, db: Session = Depends(get_db)):
    return assign_role_to_user(db, username, role_name)

@router.post("/assign-permission")
def assign_permission(username: str, permission_name: str, db: Session = Depends(get_db)):
    return assign_permission_to_user(db, username, permission_name)

