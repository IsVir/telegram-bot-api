from marshmallow import Schema, fields


class PhotoSizeSchema(Schema):
    file_id = fields.Str(required=True)
    width = fields.Int(required=True)
    height = fields.Int(required=True)
    file_size = fields.Int()
