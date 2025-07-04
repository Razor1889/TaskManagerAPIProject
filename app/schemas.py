# app/schemas.py

from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional, List

# ---------- Task Schemas ----------

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[date] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[date] = None
    is_completed: Optional[bool] = None

class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    due_date: Optional[date]
    is_completed: bool

    class Config:
        orm_mode = True

# ---------- User Schemas ----------

# Used when registering a new user
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# Used when logging in
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Used when returning a user (without password)
class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True 