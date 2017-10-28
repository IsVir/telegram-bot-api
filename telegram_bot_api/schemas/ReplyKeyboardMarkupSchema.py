from marshmallow import Schema, fields


class ReplyKeyboardMarkupSchema(Schema):
    inline_keyboard = fields.Nested('InlineKeyboardButtonSchema', many=True)