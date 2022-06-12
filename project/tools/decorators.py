from flask import request, abort
from project.config import BaseConfig
import jwt

from project.tools.implemented import user_service

config = BaseConfig()


def auth_required(func):
    """Декоратор для выполнений операций get. role=user"""
    def wrapper(*args, **kwargs):
        # Проверка авторизации и наличия токена
        if "Authorization" not in request.headers:
            abort(401)
        # Получение токена из заголовка
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
            data = jwt.decode(token, config.JWT_SECRET, algorithms=[config.JWT_ALGORITHM])
        except Exception as e:
            print('JWT decode error', e)
            abort(401)
        return func(*args, *kwargs)
    return wrapper


def admin_required(func):
    """Декоратор для операций put, post, delete. role=admin"""
    def wrapper(*args, **kwargs):
        # Проверка авторизации и наличия токена
        if "Authorization" not in request.headers:
            abort(401)

        # Получение токена из заголовка
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        role = None

        try:
            user = jwt.decode(token, config.JWT_SECRET, algorithms=[config.JWT_ALGORITHM])
            role = user.get("role")

        except Exception as e:
            print('JWT decode error', e)
            abort(401)

        # Проверка роли пользователя
        if role != 'admin':
            print(role)
            abort(403)

        return func(*args, **kwargs)
    return wrapper




