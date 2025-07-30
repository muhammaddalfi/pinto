# app/dependencies/role.py
from fastapi import Depends, HTTPException, status
from app.dependencies.auth import get_current_user
from app.db.models.user import User

def role_required(role: str):
    def dependency(user: User = Depends(get_current_user)):
        if role not in [r.name for r in user.roles]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"You must have role '{role}' to access this resource"
            )
        return user
    return dependency
