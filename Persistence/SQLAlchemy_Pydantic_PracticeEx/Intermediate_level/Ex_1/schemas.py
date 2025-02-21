# schemas.py (updated)
from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int
    email: str
    name: str

    class Config:
        from_attributes = True  # Change 'orm_mode' to 'from_attributes'

