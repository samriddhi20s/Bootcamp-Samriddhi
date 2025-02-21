import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from models import Base, User, engine
from crud import get_user_by_email, create_user

# Function to initialize the database (async)
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Function to perform async operations
async def main():
    # Initialize the database
    await init_db()

    # Create an async session
    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    # Insert a new user
    async with async_session() as session:
        new_user = {"name": "Alice Smith", "email": "alice@example.com"}
        created_user = await create_user(session, new_user)
        print(f"Created user: {created_user.name} ({created_user.email})")

    # Fetch the user by email
    async with async_session() as session:
        user = await get_user_by_email(session, "alice@example.com")
        if user:
            print(f"User found: {user.name} ({user.email})")
        else:
            print("No user found.")

# Run the async main function
if __name__ == "__main__":
    asyncio.run(main())