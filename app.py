from flask import Flask
from flask_py2neo import Py2Neo

db = Py2Neo()

def create_app(config=None):
    app = Flask(__name__)
    app.config.update({
        'PY2NEO_HOST': 'db'
    })
    app.config.update(config or {})

    db.init_app(app)

    # app.register_blueprint(bp)

    return app

app = create_app()