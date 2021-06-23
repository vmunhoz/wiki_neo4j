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
        return html

    return str(article)


@bp.route('/build_dataset/')
def build_dataset_route():
    build_dataset(db)
    return "done!"
