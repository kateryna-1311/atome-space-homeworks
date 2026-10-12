from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200


def test_get_book():
    response = client.get("/books/2")
    assert response.status_code == 200
    response = client.get("/books/100")
    assert response.status_code == 404


def test_post():
    response = client.post(
        "/books", json={"title": "cool book", "author": "cool boy", "year": 2026}
    )
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["title"] == "cool book"
    assert data["author"] == "cool boy"
    assert data["year"] == 2026
    get_response = client.get("/books")
    assert get_response.status_code == 200


def test_delete():
    response = client.delete("/books/1")
    assert response.status_code == 200
    response = client.delete("/books/999")
    assert response.status_code == 404
