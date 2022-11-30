from database.code.models.code_model import Code
from database.models.base_model import db
from database.users.models.user_model import User


def create_database():
    db.connect()
    db.create_tables([User, Code])
