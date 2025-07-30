from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.db.models.permission import Permission
from app.schemas.permission import PermissionCreate

def create_permission(db: Session, permission_in: PermissionCreate):
    existing = db.query(Permission).filter_by(name=permission_in.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Permission already exists")

    perm = Permission(
        name=permission_in.name,
        description=permission_in.description
    )
    db.add(perm)
    db.commit()
    db.refresh(perm)
    return perm
