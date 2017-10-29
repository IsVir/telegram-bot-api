from marshmallow import Schema, fields
from telegram_bot_api.schemas.base.ModelSchema import ModelSchema


class UserSchema(Schema, ModelSchema):
    __model__ = 'User'

    id = fields.Int(required=True)
    is_bot = fields.Bool(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str()
    username = fields.Str()
    language_code = fields.Str()
