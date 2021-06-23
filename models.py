from py2neo.ogm import GraphObject, Label, Property, RelatedFrom, RelatedTo


class Article(GraphObject):
    __primarykey__ = "title"

    article = Label()

    title = Property()
    text = Property()

    references = RelatedTo("Article")
