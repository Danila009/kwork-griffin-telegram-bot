from peewee import *

from database.models.base_model import BaseModel


class Code(BaseModel):
    id = PrimaryKeyField(column_name='id')
    code = TextField(column_name='code', null=False, unique=True)
    use_count = IntegerField(column_name='use_count', null=False)
    validity_period = DateTimeField(column_name='validity_period', null=False)

    class Meta:
        table_name = 'code'
