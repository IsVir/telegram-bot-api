from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int()
    is_bot = fields.Bool()
    first_name = fields.Str()
    last_name = fields.Str()
    username = fields.Str()
    language_code = fields.Str()

