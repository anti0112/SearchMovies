class MovieService:
    def __init__(self, dao):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_year(self, year):
        return self.dao.get_year(year)

    def get_director(self, director_id):
        return self.dao.get_director(director_id)

    def get_genre(self, genre_id):
        return self.dao.get_genre(genre_id)

    def create(self, data):
        self.dao.create(data)

    def update(self, data):
        self.dao.update(data)

    def delete(self, mid):
        self.dao.delete(mid)
