from marshmallow import Schema, fields


class InvoiceSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    start_parameter = fields.Str(required=True)
    currency = fields.Str(required=True)
    total_amount = fields.Int(required=True)
