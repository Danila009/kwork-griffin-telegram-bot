import peewee as pw
from peewee import Model

db = pw.MySQLDatabase(
    "u1816286_default",
    host="server35.hosting.reg.ru",
    port=3306,
    user="u1816286_default",
    passwd="kF8s6zEr7X7cNnIu")


class BaseModel(Model):
    class Meta:
        database = db
        order_by = 'id'
