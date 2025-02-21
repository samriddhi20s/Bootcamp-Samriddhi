from sqlalchemy.orm import Session
from models import User
from schemas import UserSchema

def get_users(db: Session):
    users = db.query(User).all()  # Fetch all users
    return [UserSchema.model_validate(user) for user in users]  # Convert to Pydantic models
