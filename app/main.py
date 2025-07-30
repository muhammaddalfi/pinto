from fastapi import FastAPI
from app.db.database import Base, engine
from app.db import models
from app.api import routes_auth, routes_user, routes_role, routes_permission, routes_dashboard

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(routes_auth.router)
app.include_router(routes_user.router)
app.include_router(routes_role.router)
app.include_router(routes_permission.router)
app.include_router(routes_dashboard.router)
