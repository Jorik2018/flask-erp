
from flask_erp.model.Todo import Todo


class TodoRepository:
    def get_todos(self) -> "list[Todo]":
        raise NotImplementedError