


from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# 🔹 Input Serializer
class UserSerializer(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    password: str


# 🔹 Output Serializer
class UserResponseSerializer(BaseModel):
    id: int
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    is_active: bool
    created_at: datetime