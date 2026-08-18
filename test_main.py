import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Maxwell Aybar" in response.data

def test_status(client):
    response = client.get("/api/status")
    assert response.status_code == 200
    assert response.json["status"] == "active"
