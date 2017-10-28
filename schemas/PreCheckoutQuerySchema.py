from marshmallow import Schema, fields


class PreCheckoutQuerySchema(Schema):
    id = fields.Str(required=True)
    from_user = fields.Nested('UserSchema', required=True)
    currency = fields.Str(required=True)
    total_amount = fields.Int(required=True)
    invoice_payload = fields.Str(required=True)
    shipping_option_id = fields.Str()
    order_info = fields.Nested('OrderInfoSchema')
