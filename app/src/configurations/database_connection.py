import peewee
db = peewee.MySQLDatabase(
    database='gelado',
    user='root',
    host='127.0.0.1',
    port=3306,
    password='toma')


class BaseModel(peewee.Model):

    class Meta:
        database = db
