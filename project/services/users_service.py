import base64
import hashlib
import hmac
from project.config import BaseConfig
from project.schemas.user import UserSchema


class UserService:
    def __init__(self, dao):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_by_username(self, name):
        user = self.dao.get_by_username(name)
        return UserSchema().dump(user)

    def create(self, data):
        data['password'] = self.generete_password(data['password'])
        return self.dao.create(data)

    def delete(self, uid):
        return self.dao.delete(uid)

    def generete_password(self, password):
        hash_pass = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            BaseConfig.PWD_HASH_SALT,
            BaseConfig.PWD_HASH_ITERATIONS)
        return base64.b64encode(hash_pass)

    def decoded_password(self, password):
        hash_pass = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            BaseConfig.PWD_HASH_SALT,
            BaseConfig.PWD_HASH_ITERATIONS)
        return base64.b64decode(hash_pass)

    def compare_password(self, hash_password, password):
        decoded_password = base64.b64decode(hash_password)

        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            BaseConfig.PWD_HASH_SALT,
            BaseConfig.PWD_HASH_ITERATIONS)

        print(decoded_password)

        return hmac.compare_digest(decoded_password, hash_digest)

    def change_password(self, data, token):
        password_new = self.generete_password(data['password_new'])
        email = token["email"]

        try:
            if self.compare_password(token["password"], data["password"]):
                return self.dao.update_password(email, password_new)
        except Exception as e:
            print(f"Error password:{e}")



        
        

