from flask_restx import abort, Namespace, Resource
from flask import request
from project.exceptions import ItemNotFound
from project.tools.implemented import auth_service, user_service


auth_ns = Namespace('auth')


@auth_ns.route('/login')
class AuthsView(Resource):
    def post(self):
        """Получение токена по данным пользователя"""
        data = request.json

        email = data['email']
        password = data['password']

        if None in [email, password]:
            return "", 400

        token = auth_service.generate_token(email, password)
        # acc_token = auth_service.decode_token(token, email, password)
        return token

    def put(self):
        """Запрос на обновление токена с помощью 'refresh_token'"""
        data = request.get_json()

        tokens = auth_service.approve_refresh_token(data)

        return tokens, 201


@auth_ns.route("/register")
class AuthViews(Resource):
    def post(self):
        """Регистрация нового пользователя"""
        data = request.get_json()
        user_service.create(data)

        return 'Вы зарегистрировались', 201