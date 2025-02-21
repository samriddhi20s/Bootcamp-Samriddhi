from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    age: int

    class Config:
        from_attributes = True  # Corrects the warning in Pydantic V2
