from py2neo.ogm import Model, Label, Property, RelatedFrom, RelatedTo
from model.article import Article


class Person(Model):
    __primarykey__ = "name"

    name = Property()

    likes = RelatedTo(Article)
