import requests
from flask_erp.model.Todo import Todo
from flask_erp.repository.todo_repository import TodoRepository

class TodoApiClient(TodoRepository):
    def get_todos(self) -> "list[Todo]":
        response = requests.get("https://jsonplaceholder.typicode.com/todos") 
        todos_json = response.json()
        todos: "list[Todo]" = []

        for todo_data in todos_json:
            todo = Todo(id=todo_data["id"], title=todo_data["title"], completed=todo_data["completed"])
            todos.append(todo)

        return todos