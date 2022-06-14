from marshmallow import Schema, fields


class FavoriteSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    movie_id = fields.Int()
