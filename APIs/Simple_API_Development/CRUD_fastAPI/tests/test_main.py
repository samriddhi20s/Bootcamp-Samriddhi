from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Sample item for testing
test_item = {
    "id": 1,
    "name": "Laptop",
    "description": "A high-performance laptop",
    "price": 1200.99,
    "quantity": 5
}

def test_create_item():
    response = client.post("/items/", json=test_item)
    assert response.status_code == 200
    assert response.json() == test_item

def test_get_all_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert len(response.json()) > 0  # At least one item should exist

def test_get_single_item():
    response = client.get(f"/items/{test_item['id']}")
    assert response.status_code == 200
    assert response.json()["name"] == "Laptop"

def test_update_item():
    updated_item = test_item.copy()
    updated_item["name"] = "Gaming Laptop"
    response = client.put(f"/items/{test_item['id']}", json=updated_item)
    assert response.status_code == 200
    assert response.json()["name"] == "Gaming Laptop"

def test_delete_item():
    response = client.delete(f"/items/{test_item['id']}")
    assert response.status_code == 200
    assert response.json() == {"message": "Item deleted successfully"}

def test_get_deleted_item():
    response = client.get(f"/items/{test_item['id']}")
    assert response.status_code == 404
