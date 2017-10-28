from marshmallow import Schema, fields


class MessageEntitySchema(Schema):
    type = fields.Str(required=True)
    offset = fields.Int(required=True)
    length = fields.Int(required=True)
    url = fields.Str()
    user = fields.Nested('UserSchema')
