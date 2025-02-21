from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base

# PostgreSQL database URL (async)
DATABASE_URL = "postgresql+asyncpg://user:password@localhost:5432/your_database_name"

# Create the async SQLAlchemy engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Base class for models
Base = declarative_base()

# Define the User model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)