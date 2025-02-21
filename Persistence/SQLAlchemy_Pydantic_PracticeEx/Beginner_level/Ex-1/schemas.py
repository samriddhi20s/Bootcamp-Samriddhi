from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr
    age: int

class UserCreate(UserBase):
    pass  # Inherits all fields from UserBase

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
