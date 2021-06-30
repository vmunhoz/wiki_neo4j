from py2neo.ogm import Model, Label, Property, RelatedTo
from model.article import Article


class Person(Model):
    __primarykey__ = "name"

    person = Label()

    name = Property()

    likes = RelatedTo(Article)
