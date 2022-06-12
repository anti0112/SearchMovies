from flask import request
from flask_restx import Resource, Namespace
from project.schemas.movie import MovieSchema
from project.tools.decorators import auth_required, admin_required
from project.tools.implemented import movie_service

movies_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movies_ns.route('/')
class MoviesView(Resource):
    @auth_required
    def get(self):
        """Получение всего списка фильмов, реализован поиск с условием"""
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year_id = request.args.get('year')
        status = request.args.get('status')
        page = request.args.get('page')
        if page:
            movies = movie_service.get_all_page(page)
        elif director_id:
            movies = movie_service.get_director(director_id)
        elif genre_id:
            movies = movie_service.get_genre(genre_id)
        elif year_id:
            movies = movie_service.get_year(year_id)
        else:
            movies = movie_service.get_all()
            print(movies)

        return movies_schema.dump(movies), 200

    @admin_required
    def post(self):
        """Добавление нового фильма"""
        data = request.get_json()
        movie_service.create(data)

        return "Успешно создано", 201


@movies_ns.route("/<int:mid>")
class MoviesView(Resource):
    @auth_required
    def get(self, mid):
        """Получение фильма по id"""
        movie = movie_service.get_one(mid)

        return movie_schema.dump(movie), 200

    @admin_required
    def put(self, mid):
        """Обновление информации о фильме"""
        data = request.get_json()
        data['id'] = mid

        movie_service.update(data)

        return "Успешно обновлено", 201

    @admin_required
    def delete(self, mid):
        """Удаление фильма"""
        movie_service.delete(mid)

        return "Успешно удалено", 204