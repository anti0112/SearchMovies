class FavoriteService:
    def __init__(self, dao):
        self.dao = dao

    def add_movie(self, mid, user):
        return self.dao.add_movie(mid, user)

    def delete(self, movie_id):
        return self.dao.delete(movie_id)

    def query_response(self, movie_id):
        return self.dao.query_response(movie_id)

