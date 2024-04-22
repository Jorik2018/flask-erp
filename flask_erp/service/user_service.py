
from flask_erp.model.Todo import Todo
from flask_erp.model.User import User
from sqlalchemy.orm import Session
from flask_erp.util.db import db

class UserService:

    # def __init__(self, session: Session) -> None:
    #     self._session = session

    def create(self, user: User) -> Todo:
        session: Session = db.session
        session.add(user)
        session.flush()
        return user

    def get(self, id:int) -> User:
        return db.get_or_404(User, id)
      
    def list(self, offset: int, limit: int):
        session: Session = db.session
        return session.execute(db.select(User).order_by(User.username).offset(offset).fetch(limit)).scalars()
    
    def delete(self, id:int) -> bool:
        user = db.get_or_404(User, id)
        session: Session = db.session
        session.delete(user)
        return True