from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from crud import get_users

DATABASE_URL = "sqlite:///./test.db"  # Ensure this points to your database

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# **Create Tables if they don't exist**
Base.metadata.create_all(bind=engine)

# Create DB Session
db = SessionLocal()

# Fetch and Display Users
users = get_users(db)
for user in users:
    print(user.model_dump_json(indent=4))  
    print(users)