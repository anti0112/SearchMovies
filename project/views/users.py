from flask import request
from flask_restx import Resource, Namespace

from project.schemas.user import UserSchema
from project.tools.decorators import admin_required, auth_required
from project.tools.implemented import user_service, auth_service

users_ns = Namespace('users')
user_ns = Namespace('user')


@users_ns.route('/')
class UsersView(Resource):
    def get(self):
        """Получение всех зарегистрированных пользователей"""
        users = user_service.get_all()
        return UserSchema(many=True).dump(users)


@users_ns.route('/<int:uid>')
class UserView(Resource):
    @admin_required
    def delete(self, uid):
        """Удаление пользователя только для (admin)"""
        user_service.delete(uid)
        return "", 204


@user_ns.route("/password")
class UserViews(Resource):
    @auth_required
    def put(self):
        """Смена пароля"""
        data = request.get_json()
        token = auth_service.get_data_token()

        user_service.change_password(data, token)

        return "Пароль изменен", 201


@user_ns.route('/')
class UserView(Resource):
    @auth_required
    def get(self):
        token = auth_service.get_data_token()
        user = user_service.get_by_username(token["email"])
        return UserSchema().dump(user)
