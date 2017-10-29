from marshmallow import Schema, fields
from .base.ModelSchema import ModelSchema


class ChatPhotoSchema(Schema, ModelSchema):
    __model__ = 'ChatPhoto'

    small_file_id = fields.Str(required=True)
    big_file_id = fields.Str(required=True)
