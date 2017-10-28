from marshmallow import Schema, fields


class AudioSchema(Schema):
    file_id = fields.Str(required=True)
    duration = fields.Int(required=True)
    performer = fields.Str()
    title = fields.Str()
    mime_type = fields.Str()
    file_size = fields.Int()
