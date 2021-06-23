from py2neo.ogm import Model, Label, Property, RelatedFrom, RelatedTo


class Person(Model):
    __primarykey__ = "name"

    name = Property()

    likes = RelatedTo("Article")
