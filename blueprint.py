from flask import Blueprint, app

from dataset import build_dataset
from flask_py2neo import Py2Neo
from model import Article

db = Py2Neo()
bp = Blueprint('bp', __name__)


@bp.route('/')
def index():
    article = Article()
    article.title = "Python"
    article.text = "Melhor linguagem do mundo"

    db.graph.push(article)

    return "aoba"


@bp.route('/article/<title>')
def article(title):
    article = Article.match(db.graph, title).first()
    if article:
        html = f"<h1>{article.title}</h1><p>{article.text}</p>"

        if article.references:
            html += "<p>References:</p>\n<ul>"
            for ref in article.references:
                html += f"<li><a href='/article/{ref.title}'>{ref.title}</a></li>"
            html += "</ul>"

        is_referenced_by = db.graph.run(f"MATCH (a:Article)-[r:REFERENCES]->(b:Article {{title:'{article.title}'}}) RETURN a.title").data()

        if is_referenced_by:
            html += "<p>Is referenced by:</p>\n<ul>"
            for ref in is_referenced_by:
                html += f"<li><a href='/article/{ref['a.title']}'>{ref['a.title']}</a></li>"
            html += "</ul>"

        return html

    return str(article)


@bp.route('/build_dataset/')
def build_dataset_route():
    build_dataset(db)
    return "done!"
