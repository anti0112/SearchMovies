
from flask_restx import Namespace, Resource
from project.tools.decorators import auth_required
from project.tools.implemented import favorite_service, auth_service, user_service

favorites_ns = Namespace("favorites")


@favorites_ns.route("/movies/<int:movie_id>")
class FavoritesView(Resource):
    @auth_required
    def post(self, movie_id):
        token = auth_service.get_data_token()
        user = user_service.get_by_username(token["email"])


        favorite_service.add_movie(movie_id, user)
        # favorite_service.query_response(movie_id)

        return "Успешно добавлено", 201

    @auth_required
    def delete(self, movie_id):
        token = auth_service.get_data_token()
        user = user_service.get_by_username(token["email"])

        favorite_service.delete(movie_id)

        return "Фильм удален из избранного", 200















