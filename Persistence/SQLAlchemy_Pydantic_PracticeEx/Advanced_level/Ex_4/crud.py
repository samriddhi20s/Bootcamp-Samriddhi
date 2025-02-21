from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import User
from schemas import UserSchema

# Function to fetch a user by email (async)
async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).filter(User.email == email))
    user = result.scalars().first()
    if user:
        return UserSchema.from_orm(user)
    return None

# Function to insert a new user (async)
async def create_user(db: AsyncSession, user_data: dict):
    user = User(name=user_data["name"], email=user_data["email"])
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return UserSchema.from_orm(user)