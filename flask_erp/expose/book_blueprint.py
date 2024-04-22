from flask import Blueprint

book_blueprint = Blueprint('book_blueprint', __name__, url_prefix = '/api/book')

@book_blueprint.route('/')
def index():
    return "This is an example app"