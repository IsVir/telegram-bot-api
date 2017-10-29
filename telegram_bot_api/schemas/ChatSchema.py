from marshmallow import Schema, fields
from .base.ModelSchema import ModelSchema


class ChatSchema(Schema, ModelSchema):
    __model__ = 'Chat'

    id = fields.Int(required=True, attribute='chat_id')
    type = fields.Str(required=True,
                      attribute='chat_type',
                      validate=lambda x: x in ['private', 'group', 'supergroup', 'channel'])
    title = fields.Str()
    username = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
    all_members_are_administrators = fields.Bool()
    photo = fields.Nested('ChatPhotoSchema')
    description = fields.Str()
    invite_link = fields.Str()
    pinned_message = fields.Nested('MessageSchema')
    sticker_set_name = fields.Str()
    can_set_sticker_set = fields.Bool()
