from fastapi import Depends, HTTPException, status
from app.dependencies.auth import get_current_user
from app.db.models.user import User

def permission_required(permission: str):
    def dependency(user: User = Depends(get_current_user)):
        if permission not in [perm.name for perm in user.permissions]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You don't have permission to access this resource"
            )
        return user
    return dependency
