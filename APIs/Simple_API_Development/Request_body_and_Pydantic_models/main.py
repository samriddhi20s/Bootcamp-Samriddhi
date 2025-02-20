from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# In-memory database (for simplicity)
items_db: Dict[int, dict] = {}

#  Define Pydantic model
class Item(BaseModel):
    name: str
    category: str
    price: float
    stock: int

#  Create an item (Request Body)
@app.post("/items/")
def create_item(item: Item):
    item_id = len(items_db) + 1
    items_db[item_id] = item.dict()  # Convert Pydantic model to dictionary
    return {"id": item_id, "message": "Item added successfully", "item": item}

# Get all items
@app.get("/items/")
def get_items():
    return items_db

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to FastAPI with Pydantic!"}
