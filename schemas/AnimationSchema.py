from marshmallow import Schema, fields


class AnimationSchema(Schema):
    file_id = fields.Str(required=True)
    thumb = fields.Nested('PhotoSizeSchema')
    file_name = fields.Str()
    mime_type = fields.Str()
    file_size = fields.Int()
