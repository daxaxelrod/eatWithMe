# models for users
import datetime
from flask.login import UserMixin
from peewee import *

DATABASE = SqliteDatabase('eater.db')

class BaseModel(Model):
    class Meta:
        database = DATABASE

class User(BaseModel):
    username = Charfield(unique=True)
    hungry = BooleanField()
