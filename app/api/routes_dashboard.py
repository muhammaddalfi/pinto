from fastapi import APIRouter, Depends
from app.dependencies.permission import permission_required
from app.db.models.user import User

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

@router.get("/")
def read_dashboard(
    current_user: User = Depends(permission_required("view_dashboard"))
):
    return {
        "msg": f"Welcome to your dashboard, {current_user.username}!",
        "roles": [r.name for r in current_user.roles],
        "permissions": [p.name for p in current_user.permissions]
    }
