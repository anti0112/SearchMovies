from project.dao.models.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        """Получение всех пользователей"""
        return self.session.query(User).all()

    def create(self, data):
        """Регистрация пользователя"""
        user = User(**data)

        self.session.add(user)
        self.session.commit()

        return user

    def delete(self, uid):
        """Удаление пользователя"""
        user = self.session.query(User).get(uid)

        self.session.delete(user)
        self.session.commit()

    def get_by_username(self, email):
        """Получение определенного пользователя с его данными"""
        return self.session.query(User).filter(User.email == email).first()

    def update_password(self, email, new_password):
        user = self.session.query(User).filter(User.email == email).first()
        user.password = new_password
        self.session.add(user)
        self.session.commit()



