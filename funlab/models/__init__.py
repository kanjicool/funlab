import mongoengine as me
from flask_mongoengine import MongoEngine

from.user import User

__all__ = ["User"]


db = MongoEngine()


def init_db(app):
    db.init_app(app)
