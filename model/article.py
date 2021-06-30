from py2neo.ogm import Model, Label, Property, RelatedTo


class Article(Model):
    __primarykey__ = "title"

    article = Label()

    title = Property()
    text = Property()

    references = RelatedTo("Article")
