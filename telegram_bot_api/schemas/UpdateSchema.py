from marshmallow import Schema, fields
from .base.ModelSchema import ModelSchema


class UpdateSchema(Schema, ModelSchema):
    __model__ = 'Update'

    update_id = fields.Int(required=True)
    message = fields.Nested('MessageSchema')
    edited_message = fields.Nested('MessageSchema')
    channel_post = fields.Nested('MessageSchema')
    edited_channel_post = fields.Nested('MessageSchema')
    inline_query = fields.Nested('InlineQuerySchema')
    chosen_inline_result = fields.Nested('ChosenInlineResultSchema')
    callback_query = fields.Nested('CallbackQuerySchema')
    shipping_query = fields.Nested('ShippingQuerySchema')
    pre_checkout_query = fields.Nested('PreCheckoutQuerySchema')
