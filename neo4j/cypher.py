from flask_api import Py2Neo


class Cypher:

    def __init__(self):
        self.graph = Py2Neo().graph

    def run(self, query):
        try:
            return self.graph.run(query)
        except Exception as exc:
            print(f'Error when running query: {query}. {str(exc)}')
            return None

    def match(self, query):
        try:
            match = self.graph.run(query)
            result = match.data()
            if not result:
                return []
            return result
        except Exception as exc:
            print(f'Error when running query: {query}. {str(exc)}')
            return []
