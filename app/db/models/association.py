# file ini berfungsi untuk relasi many-to-many

from sqlalchemy import Table, Column, Integer, ForeignKey
from app.db.database import Base

user_roles = Table(
    'user_roles', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('role_id', Integer, ForeignKey('roles.id'))
    
)

role_permissions = Table(
    'role_permissions', Base.metadata,
    Column('role_id',Integer, ForeignKey('roles.id')),
    Column('permission_id',Integer, ForeignKey('permissions.id'))
)

user_permissions = Table(
    'user_permissions', Base.metadata,
    Column('user_id', Integer,ForeignKey('users.id')),
    Column('permission_id', Integer,ForeignKey('permissions.id'))
)