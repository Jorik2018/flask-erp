from marshmallow import Schema, fields
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from flask_erp.util.db import db
from sqlalchemy_serializer import SerializerMixin

class User(db.Model, SerializerMixin):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]

class UserSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)
