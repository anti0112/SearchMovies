from flask import Flask
# from flask_cors import CORS
from flask_restx import Api

from project.config import DevelopmentConfig
from project.setup_db import db
from project.views import genres_ns
from project.views.auth import auth_ns
from project.views.directors import directors_ns
from project.views.movies import movies_ns
from project.views.users import users_ns, user_ns

api = Api(
    authorizations={
        "Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}
    },
    title="Flask Course Project 3",
    doc="/docs",
)

# cors = CORS()


def create_app(config_object):
    """Создание Flask app и применение конфига """
    application = Flask(__name__)
    application.config.from_object(config_object)
    application.app_context().push()
    # cors.init_app(application)
    register_extensions(application)
    return application


def register_extensions(application):
    """Подключение Api и создание namespace"""
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(users_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)


if __name__ == "__main__":
    app = create_app(DevelopmentConfig())
    app.run()
