from flask import Blueprint, jsonify
from dependency_injector.wiring import inject, Provide
from flask_erp.cbv import cbv
from flask_erp.di.di import DI
from flask_erp.model.Todo import Todo
from flask_erp.service.todo_service import TodoService

blueprint = Blueprint('todo_routes', __name__, url_prefix="/api/todo")

class TodoController:

    todo_service: TodoService = Provide[DI.todo_service]

    @blueprint.route("/test/<var>")
    def load_db(self):
        return self
    
    @blueprint.route("/<id>", methods=["GET"])
    @inject
    def get_todo(id: str, todo_service: TodoService = Provide[DI.todo_service]):
        todo: Todo = todo_service.get_todo(int(id))
        return jsonify(todo.json()), 200

def inject():
    DI().wire(modules=[__name__])