
from application.models.user import User


def createTables(db):
    """how to use: run: flask  shell, from application import db """
    db.create_all()
