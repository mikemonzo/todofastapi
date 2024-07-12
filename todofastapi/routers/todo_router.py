"""
This module defines the API routes for managing todos.
"""

from fastapi import APIRouter
from ..controllers.todo_controller import TodoController, TodoCreate

router = APIRouter()
todo_controler = TodoController()


@router.post("/todos")
def create_todo(todo: TodoCreate):
    """
    Create a new todo.
    """
    return todo_controler.create_todo(todo)


@router.get("/todos")
def get_todos():
    """
    Get all todos.
    """
    return todo_controler.get_todos()


@router.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    """
    Get a specific todo by its ID.
    """
    return todo_controler.get_todo(todo_id)


@router.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: TodoCreate):
    """
    Update a specific todo by its ID.
    """
    return todo_controler.update_todo(todo_id, updated_todo)


@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    """
    Delete a specific todo by its ID.
    """
    return todo_controler.delete_todo(todo_id)
