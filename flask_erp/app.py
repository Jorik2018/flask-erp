from flask import Flask
from flask_erp.expose.book_blueprint import book_blueprint
from flask_erp.expose import todo_blueprint, user_blueprint
from flask_erp.util.db import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:123456@localhost:5432/flask_development"
db.init_app(app)

with app.app_context():
    db.create_all()

@app.before_request
def before_request():
    """
    Opens a new database session before each request.
    """
    print('init session')
    db.session()

@app.after_request
def after_request(response):
    """
    Commits the database session and closes it after each request.
    """
    db.session.commit()
    db.session.remove()
    print('close session')
    return response

app.register_blueprint(book_blueprint)
app.register_blueprint(todo_blueprint.blueprint)
todo_blueprint.inject()
app.register_blueprint(user_blueprint.blueprint)
user_blueprint.inject()