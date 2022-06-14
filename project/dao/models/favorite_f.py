from project.dao.models.base import BaseMixin
from project.dao.models.movie import Movie
from project.dao.models.user import User
from project.setup_db import db


class Favorite(db.Model, BaseMixin):
    __tablename__ = 'favorite_genre'
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))
    user = db.relationship(User, backref=db.backref("favorite_genre", cascade="all, delete-orphan"))
    movie = db.relationship(Movie, backref=db.backref("favorite_genre", cascade="all, delete-orphan"))
