from flask import Blueprint

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
