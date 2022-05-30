from flask import request
from flask_restx import Resource, Namespace

from project.schemas.user import UserSchema
from project.tools.decorators import admin_required
from project.tools.implemented import user_service

users_ns = Namespace('users')


@users_ns.route('/')
class UsersView(Resource):
    def get(self):
        """Получение всех зарегистрированных пользователей"""
        users = user_service.get_all()
        return UserSchema(many=True).dump(users)

    def post(self):
        """Регистрация нового пользователя"""
        data = request.get_json()
        user_service.create(data)

        return 'Успешно создано', 201


@users_ns.route('/<int:uid>')
class UserView(Resource):
    @admin_required
    def delete(self, uid):
        """Удаление пользователя только для (admin)"""
        user_service.delete(uid)

        return "", 204
