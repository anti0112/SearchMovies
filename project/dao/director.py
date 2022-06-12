from project.dao.models.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        """Получение всего списка director"""
        return self.session.query(Director).all()

    def get_one(self, did):
        """Получение определенного режиссера по id"""
        return self.session.query(Director).get(did)

    def create(self, data):
        """Создание нового режиссера"""
        director = Director(**data)

        self.session.add(director)
        self.session.commit()

        return director

    def update(self, data):
        """Обновление режиссера по id"""
        did = data['id']

        director = self.get_one(did)
        if director is None:
            return "Genre not found", 404

        director.id = data['id']
        director.name = data['name']

        self.session.add(director)
        self.session.commit()

    def delete(self, did):
        """Удаление по id"""
        director = self.get_one(did)

        self.session.delete(director)
        self.session.commit()
