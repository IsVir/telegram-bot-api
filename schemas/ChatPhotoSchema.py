from marshmallow import Schema, fields


class ChatPhotoSchema(Schema):
    small_file_id = fields.Str(required=True)
    big_file_id = fields.Str(required=True)
