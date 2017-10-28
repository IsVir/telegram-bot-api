from marshmallow import Schema, fields


class InlineQuerySchema(Schema):
    id = fields.Str(required=True)
    from_user = fields.Nested('UserSchema', required=True, attribute='from')
    location = fields.Nested('LocationSchema')
    query = fields.Str(required=True)
    offset = fields.Str(required=True)
