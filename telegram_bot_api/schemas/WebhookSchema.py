from marshmallow import Schema, fields


class WebhookSchema(Schema):
    result = fields.Bool(required=True)
    description = fields.Str(required=True)
