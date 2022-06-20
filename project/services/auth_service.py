import datetime
import calendar
import jwt
from flask import request

from flask_restx import abort
from project.config import BaseConfig
from project.services.users_service import UserService


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_token(self, email, password):
        """Создание токена на основе данных пользователя"""
        user = self.user_service.get_by_username(email)

        if user is None:
            raise abort(404)

        # if not self.user_service.compare_password(user.password, password):
        #     abort(400)


        data = {
            "email": user.email,
            "role": user.role,
            "password": str(user.password)
        }

        # Выдача токена на определенное время
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, BaseConfig.JWT_SECRET, BaseConfig.JWT_ALGORITHM)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, BaseConfig.JWT_SECRET, BaseConfig.JWT_ALGORITHM)

        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    def approve_refresh_token(self, data):
        """Обновление токена с помощью (refresh_token)"""
        refresh_token = data['refresh_token']
        token = jwt.decode(jwt=refresh_token, key=BaseConfig.JWT_SECRET, algorithms=BaseConfig.JWT_ALGORITHM)
        email = token["email"]
        password = token["password"]
        print(email, password)

        return self.generate_token(email, password)

    def get_data_token(self):
        response = request.headers["Authorization"]
        token = response.split("Bearer ")[-1]
        data = jwt.decode(jwt=token, key=BaseConfig.JWT_SECRET, algorithms=BaseConfig.JWT_ALGORITHM)
        return data
