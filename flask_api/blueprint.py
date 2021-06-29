from flask import Blueprint, render_template

from model import Article, Person
from neo4j import DBHandler

bp = Blueprint('bp', __name__)


@bp.route('/')
def index():
    article = Article()
    article.title = "Python"
    article.text = "Melhor linguagem do mundo"
    DBHandler().push(article)
    return render_template('graph.html')


@bp.route('/article/<title>')
def article(title):
    db_handler = DBHandler()
    article = db_handler.get_article_by_title(Article, title)
    if article:
        is_referenced_by = db_handler.get_all_referenced_articles_by_title(title=article.title)
        if is_referenced_by is None:
            is_referenced_by = []
        return render_template('article.html', article=article, is_referenced_by=is_referenced_by)

    return str(article)


@bp.route('/person/<name>')
def person(name):
    db_handler = DBHandler()
    person = db_handler.get_person_by_name(Person, name)
    if person:
        return render_template('person.html', person=person)

    return str(person)


@bp.route('/build_dataset/')
def build_dataset_route():
    DBHandler().build_dataset()
    return "done!"
