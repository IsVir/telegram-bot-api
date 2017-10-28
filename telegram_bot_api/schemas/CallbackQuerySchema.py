from marshmallow import Schema, fields


class CallbackQuerySchema(Schema):
    id = fields.Int(required=True)
    from_user = fields.Nested('UserSchema', required=True)
    message = fields.Nested('MessageSchema')
    inline_message_id = fields.Str()
    chat_instance = fields.Str(required=True)
    data = fields.Str()
    game_short_name = fields.Str()
