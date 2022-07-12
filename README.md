## Описание проекта
- Создать виртуальное окружение
```shell
virtualenv venv
```

- Установка зависимостей
```shell
pip install -r requirements.txt
```

- Создание моделей (очистит БД и создаст все модели, указанные в импорте)
```shell
python create_tables
```

- Загрузка данных в базу
```shell
python load_fixture
```
Скрипт читает файл fixtures.json и загружает данные в базу. Если данные уже загружены - выводит соответсвующее сообщение. 

## Запуск проекта
```shell
server.py
```

## Ручное тестирование работоспособности через POSTMAN 
  https://www.postman.com/
## Запуск тестов
```shell
pytest .
```

