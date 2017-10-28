from marshmallow import Schema, fields


class ErrorSchema(Schema):
    error_code = fields.Int(required=True)
    description = fields.Str(required=True)
