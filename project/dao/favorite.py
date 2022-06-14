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

    def delete(self, movie_id):

        movie = self.session.query(Favorite).get(movie_id)
        self.session.delete(movie)
        self.session.commit()

    def query_response(self, movie_id):
        data = self.session.query(Favorite).join(Movie).filter(Movie.id == movie_id).one_or_none()
        print(data.movie_id.description)

