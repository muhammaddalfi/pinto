from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.db.models.role import Role
from app.db.models.permission import Permission
from app.schemas.role import RoleCreate

def create_role(db: Session, role_in: RoleCreate):
    existing = db.query(Role).filter_by(name=role_in.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Role already exists")
    
    role = Role(name=role_in.name, description=role_in.description)
    db.add(role)
    db.commit()
    db.refresh(role)
    return role

def get_all_roles(db: Session):
    return db.query(Role).all()

def assign_permission_to_role(db: Session, role_name: str, permission_name: str):
    role = db.query(Role).filter_by(name=role_name).first()
    perm = db.query(Permission).filter_by(name=permission_name).first()

    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    if not perm:
        raise HTTPException(status_code=404, detail="Permission not found")

    if perm in role.permissions:
        return {"msg": "Permission already assigned to role"}

    role.permissions.append(perm)
    db.commit()
    return {"msg": f"Permission '{permission_name}' assigned to role '{role_name}'"}
