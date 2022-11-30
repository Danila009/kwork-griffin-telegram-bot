from peewee import *

from database.models.base_model import BaseModel


class Code(BaseModel):
    id = PrimaryKeyField(column_name='id')
    code = TextField(column_name='code', null=False, unique=True)

    class Meta:
        table_name = 'code'
