from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.db.models.user import User
from app.db.models.role import Role
from app.db.models.permission import Permission

def assign_role_to_user(db: Session, username: str, role_name: str):
    user = db.query(User).filter_by(username=username).first()
    role = db.query(Role).filter_by(name=role_name).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    if role in user.roles:
        return {"msg": "User already has this role"}

    user.roles.append(role)
    db.commit()
    return {"msg": f"Role '{role_name}' assigned to user '{username}'"}

def assign_permission_to_user(db: Session, username: str, permission_name: str):
    user = db.query(User).filter_by(username=username).first()
    perm = db.query(Permission).filter_by(name=permission_name).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not perm:
        raise HTTPException(status_code=404, detail="Permission not found")

    if perm in user.permissions:
        return {"msg": "Permission already assigned to user"}

    user.permissions.append(perm)
    db.commit()
    return {"msg": f"Permission '{permission_name}' assigned to user '{username}'"}
