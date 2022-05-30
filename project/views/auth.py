from flask_restx import abort, Namespace, Resource
from flask import request
from project.exceptions import ItemNotFound
from project.tools.implemented import auth_service
from project.setup_db import db

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthsView(Resource):
    def post(self):
        """Получение токена по данным пользователя"""
        data = request.json

        email = data.get('email', None)
        password = data.get('password', None)
        print(email, password)
        if None in [email, password]:
            return "", 400

        token = auth_service.generate_token(email, password)
        return token

    def put(self):
        """Запрос на обновление токена с помощью 'refresh_token'"""
        data = request.get_json()
        token = data.get('refresh_token')

        tokens = auth_service.approve_refresh_token(token)

        return tokens, 201