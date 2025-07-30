from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base

class Permission(Base):
    __tablename__ = 'permissions'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True)
    description = Column(String(255))

    roles = relationship("Role", secondary="role_permissions", back_populates="permissions")
    users = relationship("User", secondary="user_permissions", back_populates="permissions")
