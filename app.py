from time import sleep

from flask import Flask

from flask_api import Py2Neo
from flask_api.blueprint import bp


def create_app(config=None):
    app = Flask(__name__)
    app.config.update({
        'PY2NEO_HOST': 'db'
    })
    app.config.update(config or {})

    db = Py2Neo()
    db.init_app(app)

    app.register_blueprint(bp)

    @app.before_first_request
    def function_to_run_only_once():
        from neo4j import DBHandler
        DBHandler().build_dataset()
        print("dataset built!", flush=True)

    return app


sleep(10)
app = create_app()
