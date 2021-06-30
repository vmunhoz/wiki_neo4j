from neo4j import Cypher, build_dataset
from flask_api import Py2Neo
from util import Singleton


class DBHandler(metaclass=Singleton):

    def __init__(self):
        self.graph = Py2Neo().graph
        self.cypher = Cypher()

    def push(self, obj):
        self.graph.push(obj)

    def match(self, **kwargs):
        model = kwargs['model']
        property = kwargs['property']
        return model.match(self.graph, property)

    def get_article_by_title(self, article_obj, title: str):
        return self.match(model=article_obj, property=title).first()

    def get_person_by_name(self, person_obj, name: str):
        return self.match(model=person_obj, property=name).first()

    def get_all_referenced_articles_by_title(self, title: str):
        query = f"""
                MATCH (a:Article)-
                    [r:REFERENCES]->
                    (b:Article {{title:'{title}'}}) 
                RETURN a.title
                """
        return self.cypher.match(query)

    def get_people_who_liked_article(self, title: str):
        query = f"""
                MATCH (p:Person)-
                    [l:LIKES]->
                    (a:Article {{title: '{title}'}}) 
                RETURN p.name, l.date
                """
        return self.cypher.match(query)

    def build_dataset(self):
        build_dataset(self)
