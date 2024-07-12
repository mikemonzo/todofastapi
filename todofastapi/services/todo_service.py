"""
This module contains the TodoService class and related models for managing todos.

TodoCreate: A pydantic BaseModel representing the data required to create a new todo.
Todo: A derived class from TodoCreate, representing a todo item with additional properties.
TodoService: A class that provides methods for creating, retrieving, updating, and deleting todos.
"""

from ..repositories.todo_repository import TodoRepository, TodoCreate, Todo


class TodoService:
    """
    A class that provides methods for creating, retrieving, updating, and deleting todos.
    """
    def __init__(self):
        self.todo_repository = TodoRepository()

    def create_todo(self, todo: TodoCreate) -> Todo:
        """
        Create a new todo.

        Args:
            todo (TodoCreate): The data required to create a new todo.

        Returns:
            Todo: The created todo.
        """
        return self.todo_repository.create_todo(todo)

    def get_todos(self) -> list[Todo]:
        """
        Get all todos.

        Returns:
            list[Todo]: A list of all todos.
        """
        return self.todo_repository.get_todos()

    def get_todo(self, todo_id: int) -> Todo | None:
        """
        Get a specific todo by its ID.

        Args:
            todo_id (int): The ID of the todo to retrieve.

        Returns:
            Todo | None: The todo with the specified ID, or None if not found.
        """
        return self.todo_repository.get_todo_by_id(todo_id)

    def update_todo(self, todo_id: int, updated_todo: TodoCreate) -> Todo | None:
        """
        Update a specific todo.

        Args:
            todo_id (int): The ID of the todo to update.
            updated_todo (TodoCreate): The updated data for the todo.

        Returns:
            Todo | None: The updated todo, or None if not found.
        """
        return self.todo_repository.update_todo_by_id(todo_id, updated_todo)

    def delete_todo(self, todo_id: int):
        """
        Delete a specific todo.

        Args:
            todo_id (int): The ID of the todo to delete.

        Returns:
            bool: True if the todo was successfully deleted, False otherwise.
        """
        return self.todo_repository.delete_todo_by_id(todo_id)
