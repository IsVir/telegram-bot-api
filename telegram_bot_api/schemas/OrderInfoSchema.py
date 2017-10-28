from marshmallow import Schema, fields


class OrderInfoSchema(Schema):
    name = fields.Str()
    phone_number = fields.Str()
    email = fields.Str()
    shipping_address = fields.Nested('ShippingAddressSchema')
