from peewee import *

from database.models.base_model import BaseModel


class User(BaseModel):
    user_id = PrimaryKeyField(column_name='id')
    login = TextField(column_name='login', null=False)
    code = TextField(column_name='code', null=False)
    token = TextField(column_name='token', null=False)
    create_date = DateField(column_name='create_date', null=False)

    class Meta:
        table_name = 'users'
