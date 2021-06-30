from flask import Blueprint, render_template, app

from model import Article, Person
from neo4j import DBHandler

bp = Blueprint('bp', __name__)


@bp.route('/')
def index():
    db_handler = DBHandler()
    articles = db_handler.get_all_articles()
    persons = db_handler.get_all_persons()
    return render_template('graph.html', articles=articles, persons=persons)


@bp.route('/article/<title>')
def article(title):
    db_handler = DBHandler()
    article = db_handler.get_article_by_title(Article, title)
    if article:
        is_referenced_by = db_handler.get_all_referenced_articles_by_title(title=article.title)
        is_liked_by = db_handler.get_people_who_liked_article(title=article.title)
        return render_template('article.html', article=article, is_referenced_by=is_referenced_by, is_liked_by=is_liked_by)

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
