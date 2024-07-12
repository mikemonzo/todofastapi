"""
This module contains the TodoController class and related models for managing todos.

The TodoController class provides methods for creating, retrieving, updating, and deleting todos.
"""

from fastapi import HTTPException
from ..services.todo_service import TodoService, TodoCreate, Todo


class TodoController:
    """
    A class that provides methods for creating, retrieving, updating, and deleting todos.
    """
    def __init__(self):
        self.todo_service = TodoService()


    def create_todo(self, todo: TodoCreate) -> Todo:
        """
        Create a new todo.

        Args:
            todo (TodoCreate): The todo data.

        Returns:
            Todo: The created todo.
        """
        return self.todo_service.create_todo(todo)


    def get_todos(self) -> list[Todo]:
        """
        Get all todos.

        Returns:
            list[Todo]: The list of todos.
        """
        return self.todo_service.get_todos()


    def get_todo(self, todo_id: int) -> Todo:
        """
        Get a todo by ID.

        Args:
            todo_id (int): The ID of the todo.

        Returns:
            Todo: The todo with the specified ID.

        Raises:
            HTTPException: If the todo is not found.
        """
        todo = self.todo_service.get_todo(todo_id)
        if todo is None:
            raise HTTPException(status_code=404, detail="Todo not found")
        return todo


    def update_todo(self, todo_id: int, update_todo: TodoCreate) -> Todo:
        """
        Update a todo.

        Args:
            todo_id (int): The ID of the todo to update.
            update_todo (TodoCreate): The updated todo data.

        Returns:
            Todo: The updated todo.

        Raises:
            HTTPException: If the todo is not found.
        """
        todo = self.todo_service.update_todo(todo_id, update_todo)
        if todo is None:
            raise HTTPException(status_code=404, detail="Todo not found")
        return todo


    def delete_todo(self, todo_id: int):
        """
        Delete a todo.

        Args:
            todo_id (int): The ID of the todo to delete.

        Raises:
            HTTPException: If the todo is not found.
        """
        if not self.todo_service.delete_todo(todo_id):
            raise HTTPException(status_code=404, detail="Todo not found")
        return {"message": "Todo deleted successfully"}
