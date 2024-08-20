# from fastapi.testclient import TestClient
# from app.main import app

# client = TestClient(app)

# def test_create_item():
#     response = client.post("/items/", json={"name": "testitem", "description": "test description"})
#     assert response.status_code == 200
#     assert response.json()["name"] == "testitem"
