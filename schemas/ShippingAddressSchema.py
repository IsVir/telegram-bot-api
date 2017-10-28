from marshmallow import Schema, fields


class ShippingAddressSchema(Schema):
    country_code = fields.Str(required=True)
    state = fields.Str(required=True)
    city = fields.Str(required=True)
    street_line1 = fields.Str(required=True)
    street_line2 = fields.Str(required=True)
    post_code = fields.Str(required=True)
