# from fastapi.testclient import TestClient
# from src.main import api

# client = TestClient(api)


# # Test home endpoint
# def test_home():
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"Message": "Hello World"}


# # Test POST
# def test_create_todo():
#     response = client.post("/todo", json={
#         "id": 1,
#         "name": "Study",
#         "des": "Prepare for exams"
#     })
#     assert response.status_code == 200
#     assert response.json()[0]["name"] == "Study"


# # Test GET all
# def test_get_todos():
#     response = client.get("/todo")
#     assert response.status_code == 200
#     assert isinstance(response.json(), list)
#     assert len(response.json()) > 0


# # Test PUT
# def test_update_todo():
#     response = client.put("/todo/1", json={
#         "id": 1,
#         "name": "Study Updated",
#         "des": "Prepare for math exams"
#     })
#     assert response.status_code == 200
#     assert response.json()[0]["name"] == "Study Updated"


# # Test DELETE
# def test_delete_todo():
#     response = client.delete("/todo/1")
#     assert response.status_code == 200
#     assert response.json() == {
#         "id": 1,
#         "name": "Study Updated",
#         "des": "Prepare for math exams"
#     }

from fastapi.testclient import TestClient
from src.main import api  

client = TestClient(api)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "Welcome to the Book Management System"}


def test_add_book():
    response = client.post("/book", json={
        "id": 1,
        "name": "Python 101",
        "description": "Beginner friendly Python book",
        "isAvailable": True
    })
    assert response.status_code == 200
    data = response.json()
    assert any(book["id"] == 1 for book in data)


def test_get_books():
    response = client.get("/book")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_update_book():
    response = client.put("/book/1", json={
        "id": 1,
        "name": "Python Advanced",
        "description": "Advanced concepts in Python",
        "isAvailable": False
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Python Advanced"
    assert data["isAvailable"] is False


def test_delete_book():
    response = client.delete("/book/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1

 
    response = client.delete("/book/1")
    assert response.json() == {"error": "Book not found, deletion failed"}
