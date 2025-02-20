from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory storage
items_db = []

# Pydantic model for Item
class Item(BaseModel):
    id: int
    name: str
    description: str = None
    price: float
    quantity: int

# Create an item
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    items_db.append(item)
    return item

# Read all items
@app.get("/items/", response_model=list[Item])
def get_items():
    return items_db

# Read a single item by ID
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# Update an item
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            items_db[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

# Delete an item
@app.delete("/items/{item_id}", response_model=dict)
def delete_item(item_id: int):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            items_db.pop(index)
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI CRUD Example!"}
