"""
This module contains the TodoRepository class and related models for managing todos.
"""

from pydantic import BaseModel

class TodoCreate(BaseModel):
    """
    A pydantic BaseModel representing the data required to create a new todo.
    """

    title: str


class Todo(TodoCreate):
    """
    A derived class from TodoCreate, representing a todo item with additional properties.
    """

    id: int
    completed: bool = False


class TodoRepository:
    """
    A class that provides methods for managing todos.
    """

    def __init__(self):
        self.todos = []

    def create_todo(self, todo: TodoCreate) -> Todo:
        """
        Creates a new todo item.

        Args:
            todo (TodoCreate): The data required to create a new todo.

        Returns:
            Todo: The created todo item.
        """
        new_todo = Todo(
            id=len(self.todos) + 1,
            **todo.model_dump(),
        )
        self.todos.append(new_todo)
        return new_todo

    def get_todos(self) -> list[Todo]:
        """
        Retrieves all the todos.

        Returns:
            list[Todo]: A list of all the todos.
        """
        return self.todos

    def get_todo_by_id(self, todo_id: int) -> Todo | None:
        """
        Retrieves a todo item by its ID.

        Args:
            todo_id (int): The ID of the todo item.

        Returns:
            Todo | None: The todo item if found, None otherwise.
        """
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None

    def update_todo_by_id(self, todo_id: int, updated_todo: TodoCreate) -> Todo | None:
        """
        Updates a todo item by its ID.

        Args:
            todo_id (int): The ID of the todo item.
            updated_todo (TodoCreate): The updated data for the todo item.

        Returns:
            Todo | None: The updated todo item if found, None otherwise.
        """
        for todo in self.todos:
            if todo.id == todo_id:
                todo.title = updated_todo.title
                return todo
        return None

    def delete_todo_by_id(self, todo_id: int) -> bool:
        """
        Deletes a todo item by its ID.

        Args:
            todo_id (int): The ID of the todo item.

        Returns:
            bool: True if the todo item was deleted successfully, False otherwise.
        """
        for todo in self.todos:
            if todo.id == todo_id:
                self.todos.remove(todo)
                return True
        return False
