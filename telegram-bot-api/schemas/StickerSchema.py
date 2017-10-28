from marshmallow import Schema, fields


class StickerSchema(Schema):
    file_id = fields.Str(required=True)
    width = fields.Int(required=True)
    height = fields.Int(required=True)
    thumb = fields.Nested('PhotoSizeSchema')
    emoji = fields.Str()
    set_name = fields.Str()
    mask_position = fields.Nested('MaskPositionSchema')
    file_size = fields.Int()
