from marshmallow import Schema, fields


class InlineKeyboardButtonSchema(Schema):
    text = fields.Str(required=True)
    url = fields.Str()
    callback_data = fields.Str()
    switch_inline_query = fields.Str()
    switch_inline_query_current_chat = fields.Str()
    callback_game = fields.Str()
    pay = fields.Str()
