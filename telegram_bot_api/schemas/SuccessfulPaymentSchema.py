from marshmallow import Schema, fields


class SuccessfulPaymentSchema(Schema):
    currency = fields.Str(required=True)
    total_amount = fields.Int(required=True)
    invoice_payload = fields.Str(required=True)
    shipping_option_id = fields.Str()
    order_info = fields.Nested('OrderInfoSchema')
    telegram_payment_charge_id = fields.Str(required=True)
    provider_payment_charge_id = fields.Str(required=True)
