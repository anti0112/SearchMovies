from project.dao.models.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        """Получение всего списка с фильмами """
        return self.session.query(Movie).all()

    def get_one(self, mid):
        """Получение определенного фильма по id"""
        return self.session.query(Movie).get(mid)

    def get_year(self, year):
        """Получение фильма по году выпуска"""
        return Movie.query.filter(Movie.year == year)

    def get_director(self, director_id):
        """Получение фильма по id director"""
        return Movie.query.filter(Movie.director_id == director_id)

    def get_genre(self, genre_id):
        """Получение фильма по id genre"""
        return Movie.query.filter(Movie.genre_id == genre_id)

    def create(self, data):
        """Создание нового фильма"""
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()

        return movie

    def update(self, data):
        """Обновление фильма по id"""
        mid = data["id"]
        movie = self.get_one(mid)
        if movie is None:
            return "Movie not found", 404
        movie.id = data['id']
        movie.title = data['title']
        movie.description = data['description']
        movie.trailer = data['trailer']
        movie.year = data['year']
        movie.rating = data['rating']
        movie.genre_id = data['genre_id']
        movie.director_id = data['director_id']

        self.session.add(movie)
        self.session.commit()

    def delete(self, mid):
        """Удаление фильма по id"""
        movie = self.get_one(mid)

        self.session.delete(movie)
        self.session.commit()


