from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base
from app.db.models.association import user_roles, user_permissions

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(128))
    
    roles = relationship("Role", secondary=user_roles, back_populates="users")
    permissions = relationship("Permission", secondary=user_permissions,back_populates="users")