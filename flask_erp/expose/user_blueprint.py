from flask import Blueprint, jsonify, request
from dependency_injector.wiring import inject, Provide
from flask_erp.di.di import DI
from flask_erp.model.Todo import Todo
from flask_erp.model.User import User, UserSchema
from flask_erp.service.todo_service import TodoService
from flask_erp.service.user_service import UserService
from flask_erp.util import json_to_entity
from flask_erp.util.db import db

blueprint = Blueprint('userroutes', __name__, url_prefix="/api/user")

class UserController:
    
    @blueprint.route("/<offset>/<limit>")
    @inject
    def list(offset: int, limit: int, user_service: UserService = Provide[DI.user_service]):
        users = user_service.list(offset, limit)
        users = [row.to_dict() for row in users]
        return jsonify(users), 200

    @blueprint.route("", methods=["POST", "PUT"])
    @inject
    def post(user_service: UserService = Provide[DI.user_service]):
        return user_service.create(json_to_entity(request.json, User)).to_dict()

    @blueprint.route("/<int:id>")
    @inject
    def get(id, user_service: UserService = Provide[DI.user_service]):
        return user_service.get(id).to_dict()

    @blueprint.route("/<int:id>", methods=["DELETE"])
    @inject
    def delete(id, user_service: UserService = Provide[DI.user_service]):
        return str(user_service.delete(id))

def inject():
    DI().wire(modules=[__name__])