# main.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from models import User
from schemas import UserSchema
from fastapi import FastAPI

app = FastAPI()  # Ensure this is named 'app'


def get_user_by_email(db: Session, email: str):
    try:
        # Query the database for the user with the given email
        user = db.query(User).filter(User.email == email).first()

        if user is None:
            # Return a message indicating user was not found
            return {"detail": "User not found"}
        
        # Return the user as a UserSchema response
        return UserSchema.from_orm(user)
    
    except Exception as e:
        return {"detail": f"An error occurred: {str(e)}"}
