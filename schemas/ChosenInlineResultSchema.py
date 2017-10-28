from marshmallow import Schema, fields


class ChosenInlineResultSchema(Schema):
    result_id = fields.Str(required=True)
    from_user = fields.Nested('UserSchema', required=True, attribute='from')
    location = fields.Nested('LocationSchema')
    inline_message_id = fields.Str()
    query = fields.Str(required=True)
