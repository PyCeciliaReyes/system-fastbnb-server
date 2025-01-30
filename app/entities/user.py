from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id: Optional[int] = None
    name: str
    email: EmailStr
    email_verified_at: Optional[datetime] = None
    password: str
    phone_number: str
    description: Optional[str] = None
    profile_image: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None