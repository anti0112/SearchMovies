from flask import request
from flask_restx import Namespace, Resource

from project.tools.decorators import auth_required, admin_required
from project.tools.implemented import director_service

from project.schemas.director import DirectorSchema

directors_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@directors_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        """Получение всех режиссеров """
        director = director_service.get_all()
        return directors_schema.dump(director), 200

    @admin_required
    def post(self):
        """Добавление нового режиссера в БД"""
        data = request.get_json()
        director_service.create(data)
        return "Успешно создано", 201


@directors_ns.route("/<int:did>")
class DirectorView(Resource):
    @auth_required
    def get(self, did):
        """Получение одного режиссера по id"""
        director = director_service.get_one(did)
        return director_schema.dump(director), 200

    @admin_required
    def put(self, did):
        """Обновление данных о режиссере"""
        data = request.get_json()
        data['id'] = did

        director_service.update(data)

        return "Успешно обновлено"

    @admin_required
    def delete(self, did):
        """Удаление режиссера из БД"""
        director_service.delete(did)

        return "Удалено", 204