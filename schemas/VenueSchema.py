from marshmallow import Schema, fields


class VenueSchema(Schema):
    location = fields.Nested('LocationSchema', required=True)
    title = fields.Str(required=True)
    address = fields.Str(required=True)
    foursquare_id = fields.Str()
