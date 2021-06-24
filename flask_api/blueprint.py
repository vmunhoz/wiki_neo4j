from flask import Blueprint

from neo4j import build_dataset
from model import Article
from neo4j import DBHandler

bp = Blueprint('bp', __name__)


@bp.route('/')
def index():
    article = Article()
    article.title = "Python"
    article.text = "Melhor linguagem do mundo"
    DBHandler().push(article)
    return "aoba"


@bp.route('/article/<title>')
def article(title):
    db_handler = DBHandler()
    article = db_handler.get_article_by_title(Article, title)
    if article:
        html = f"<h1>{article.title}</h1><p>{article.text}</p>"

        if article.references:
            html += "<p>References:</p>\n<ul>"
            for ref in article.references:
                html += f"<li><a href='/article/{ref.title}'>{ref.title}</a></li>"
            html += "</ul>"

        is_referenced_by = db_handler.get_all_referenced_articles_by_title(title=article.title)
        if is_referenced_by:
            html += "<p>Is referenced by:</p>\n<ul>"
            for ref in is_referenced_by:
                html += f"<li><a href='/article/{ref['a.title']}'>{ref['a.title']}</a></li>"
            html += "</ul>"

        return html

    return str(article)


@bp.route('/build_dataset/')
def build_dataset_route():
    build_dataset(DBHandler())
    return "done!"
