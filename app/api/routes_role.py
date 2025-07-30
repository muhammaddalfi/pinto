from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.role import RoleCreate
from app.services.role_service import (
    create_role,
    get_all_roles,
    assign_permission_to_role
)
from app.db.database import get_db

router = APIRouter(prefix="/roles", tags=["roles"])

@router.post("/")
def create(role_in: RoleCreate, db: Session = Depends(get_db)):
    return create_role(db, role_in)

@router.get("/")
def get_roles(db: Session = Depends(get_db)):
    return get_all_roles(db)

@router.post("/assign-permission")
def assign_permission(role_name: str, permission_name: str, db: Session = Depends(get_db)):
    return assign_permission_to_role(db, role_name, permission_name)
