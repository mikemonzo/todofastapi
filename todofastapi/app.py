"""
This module implements a FastAPI application for managing todo items.

It provides endpoints for creating, retrieving, updating, and deleting todo items.
"""

from fastapi import FastAPI
from .routers import todo_router

app = FastAPI()

app.include_router(todo_router.router)


# Run the app with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=3000, reload=True)
