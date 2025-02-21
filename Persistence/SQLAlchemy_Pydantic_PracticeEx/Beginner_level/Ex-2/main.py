from database import SessionLocal, engine, Base
from models import User
from schemas import UserCreate
from crud import create_user, get_users

# Create tables in database
Base.metadata.create_all(bind=engine)

# Create a new session
db = SessionLocal()

# Insert a new user
new_user = UserCreate(name="Alice", email="alice@example.com", age=28)
created_user = create_user(db, new_user)
print(f"Inserted: {created_user.id} - {created_user.name}")

# Fetch users
users = get_users(db)
for user in users:
    print(f"User: {user.id} - {user.name} - {user.email}")

db.close()
