from marshmallow import Schema, fields
from telegram_bot_api.schemas.base.ModelSchema import ModelSchema


class MessageEntitySchema(Schema, ModelSchema):
    __model__ = 'MessageEntity'

    type = fields.Str(required=True)
    offset = fields.Int(required=True)
    length = fields.Int(required=True)
    url = fields.Str()
    user = fields.Nested('UserSchema')
