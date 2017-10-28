from marshmallow import Schema, fields


class ContactSchema(Schema):
    phone_number = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str()
    user_id = fields.Int()
