from project.dao import GenreDAO
from project.dao.director import DirectorDAO
from project.dao.favorite import FavoriteDAO
from project.dao.models.favorite_f import Favorite
from project.dao.movie import MovieDAO
from project.dao.user import UserDAO
from project.services import GenresService, favorite_service
from project.services.auth_service import AuthService
from project.services.directors_service import DirectorService
from project.services.favorite_service import FavoriteService
from project.services.movie_service import MovieService
from project.services.users_service import UserService
from project.setup_db import db

movie_dao = MovieDAO(session=db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDAO(session=db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(session=db.session)
genre_service = GenresService(genre_dao)

user_dao = UserDAO(session=db.session)
user_service = UserService(user_dao)

favorite_dao = FavoriteDAO(session=db.session)
favorite_service = FavoriteService(favorite_dao)

auth_service = AuthService(UserService(user_dao))
