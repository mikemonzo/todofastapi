"""
This module contains unit tests for the Todo FastAPI application.

The tests cover the following functionalities:
- Creating a new todo
- Getting all todos
- Getting a specific todo
- Updating a todo
- Deleting a todo

Each test asserts the expected response status code and JSON payload.

"""

# import pytest
from fastapi.testclient import TestClient
from todofastapi.app import app


client = TestClient(app)


def test_create_todo():
    """
    Test case for creating a new todo.

    This function sends a POST request to the '/todos' endpoint with a JSON payload
    containing the title of the todo to be created. It then asserts that the response
    status code is 200 and the response JSON matches the expected values for the created todo.

    """
    response = client.post("/todos", json={"title": "Buy groceries"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "Buy groceries", "completed": False}


def test_get_todos():
    """
    Test case for GET /todos endpoint.
    """
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "title": "Buy groceries", "completed": False}]



def test_get_todo():
    """
    Test case for getting a specific todo by ID.
    """
    response = client.get("/todos/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "Buy groceries", "completed": False}


def test_get_todo_not_found():
    """
    Test case to verify that a 404 status code and the correct error message
    are returned when trying to retrieve a non-existent todo.
    """
    response = client.get("/todos/2")
    assert response.status_code == 404
    assert response.json() == {"detail": "Todo not found"}


def test_update_todo():
    """
    Test case for updating a todo item.

    Sends a PUT request to the "/todos/1" endpoint with a JSON payload containing the updated title.
    Asserts that the response status code is 200 and the response JSON matches the expected values.

    """
    response = client.put("/todos/1", json={"title": "Buy groceries and milk"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "Buy groceries and milk", "completed": False}


def test_update_todo_not_found():
    """
    Test case to verify the behavior when updating a non-existent todo.

    Sends a PUT request to the "/todos/2" endpoint with a JSON payload containing 
    the updated todo title.
    Asserts that the response status code is 404 (Not Found) and the response JSON contains 
    the expected error detail.

    """
    response = client.put("/todos/2", json={"title": "Buy groceries and milk"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Todo not found"}


def test_delete_todo():
    """
    Test case for deleting a todo.

    This function sends a DELETE request to the "/todos/1" endpoint and asserts that the response
    status code is 200 and the response JSON is {"message": "Todo deleted successfully"}.

    """
    response = client.delete("/todos/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Todo deleted successfully"}


def test_delete_todo_not_found():
    """
    Test case to verify that deleting a non-existent todo returns a 404 status code
    and a JSON response with the detail message "Todo not found".
    """
    response = client.delete("/todos/2")
    assert response.status_code == 404
    assert response.json() == {"detail": "Todo not found"}
