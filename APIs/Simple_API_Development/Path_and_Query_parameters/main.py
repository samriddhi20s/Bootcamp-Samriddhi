from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# Sample data
items = {
    1: {"name": "Laptop", "category": "Electronics", "price": 1200.99},
    2: {"name": "Smartphone", "category": "Electronics", "price": 800.50},
    3: {"name": "Shoes", "category": "Fashion", "price": 99.99},
}

# Path parameter: Get item by ID
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return items.get(item_id, {"error": "Item not found"})

# Path and Query parameters: Filter items by category (optional)
@app.get("/items/")
def get_filtered_items(category: Optional[str] = None, min_price: Optional[float] = None):
    filtered_items = [
        {"id": key, **value}
        for key, value in items.items()
        if (category is None or value["category"].lower() == category.lower()) and
           (min_price is None or value["price"] >= min_price)
    ]
    return filtered_items if filtered_items else {"message": "No items match the criteria"}

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Path & Query Parameters Example!"}
