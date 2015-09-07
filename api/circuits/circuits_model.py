from peewee import *


class CircuitsModel(Model):
    # just some example fields, I'll think about this later
    name = CharField()
    is_popular = BooleanField()
    created = DateField()
