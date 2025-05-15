from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr
    age: Optional[int] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None

class UserInDB(UserBase):
    id: int
    is_active: Optional[bool] = True  # optional if you have this column

    class Config:
        orm_mode = True  # <-- Corrected from `from_attributes` to `orm_mode`
