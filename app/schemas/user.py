from pydantic import BaseModel
from typing import List

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(UserCreate):
    pass

class UserOute(BaseModel):
    id: int
    username: str
    roles: List[str]
    permissions:List[str]
    class Config:
        orm_mode = True