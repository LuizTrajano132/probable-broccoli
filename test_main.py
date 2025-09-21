

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_read_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "q": None}

def test_read_item_with_query():
    response = client.get("/items/2?q=test")
    assert response.status_code == 200
    assert response.json() == {"item_id": 2, "q": "test"}

def test_create_item():
    response = client.post("/items/", json={"name": "test_item"})
    assert response.status_code == 200
    assert response.json() == {"message": "Item created", "name": "test_item"}

def test_post_data_with_validation():
    response = client.post("/items/", json={"name": "test_item", "description": "some_description"})
    assert response.status_code == 200
    assert "description" in response.json()    