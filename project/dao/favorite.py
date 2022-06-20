from project.dao.models.favorite_f import Favorite
from project.dao.models.movie import Movie


class FavoriteDAO:
    def __init__(self, session):
        self.session = session

    def add_movie(self, movie_id, user):

        data = {
            "user_id": user.id,
            "movie_id": movie_id
        }
        favorite_movie = Favorite(**data)
        self.session.add(favorite_movie)
        self.session.commit()

    def delete(self, user, movie_id):

        movie = self.session.query(Favorite).filter(
            Favorite.movie_id == movie_id and
            Favorite.user_id == user.id).first()

        self.session.delete(movie)
        self.session.commit()


