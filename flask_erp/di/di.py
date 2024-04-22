from dependency_injector import containers, providers
from flask_erp.client.todo_client import TodoApiClient
from flask_erp.service.todo_service import TodoService
from flask_erp.service.user_service import UserService
from flask_erp.util.db import db


class DI(containers.DeclarativeContainer):
    todo_api_client = providers.Factory(TodoApiClient)
    todo_service = providers.Factory(TodoService, todo_repository=todo_api_client)
    session = providers.Singleton(db.session)
    _db = db
    user_service = providers.Factory(UserService)#, session=session)
    