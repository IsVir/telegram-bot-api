from marshmallow import Schema, fields


class InlineKeyboardMarkupSchema(Schema):
    inline_keyboard = fields.List(fields.Nested('InlineKeyboardButtonSchema', many=True))