from marshmallow import Schema, fields


class ShippingQuerySchema(Schema):
    id = fields.Str(required=True)
    from_user = fields.Nested('UserSchema', attribute='from', required=True)
    invoice_payload = fields.Str(required=True)
    shipping_address = fields.Nested('ShippingAddressSchema', required=True)
