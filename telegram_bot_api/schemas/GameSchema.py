from marshmallow import Schema, fields


class GameSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    photo = fields.Nested('PhotoSizeSchema', many=True, required=True)
    text = fields.Str()
    text_entities = fields.Nested('MessageEntitySchema', many=True)
    animation = fields.Nested('AnimationSchema')
