from marshmallow import Schema, fields


class LocationSchema(Schema):
    longitude = fields.Float()
    latitude = fields.Float()
