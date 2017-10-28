from marshmallow import Schema, fields


class VoiceSchema(Schema):
    file_id = fields.Str(required=True)
    length = fields.Int(required=True)
    duration = fields.Int(required=True)
    thumb = fields.Nested('PhotoSizeSchema')
    file_size = fields.Int()
