from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.permission import PermissionCreate
from app.services.permission_service import create_permission
from app.db.database import get_db

router = APIRouter(prefix="/permissions", tags=["permissions"])

@router.post("/")
def create(permission_in: PermissionCreate, db: Session = Depends(get_db)):
    return create_permission(db, permission_in)
