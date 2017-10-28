from marshmallow import Schema, fields


class VideoSchema(Schema):
    file_id = fields.Str(required=True)
    width = fields.Int(required=True)
    height = fields.Int(required=True)
    duration = fields.Int(required=True)
    thumb = fields.Nested('PhotoSizeSchema')
    mime_type = fields.Str()
    file_size = fields.Int()
