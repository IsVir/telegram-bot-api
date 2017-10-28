from marshmallow import Schema, fields


class ChatSchema(Schema):
    id = fields.Int(required=True)
    type = fields.Str(required=True, validate=lambda x: x in ['private', 'group', 'supergroup', 'channel'])
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
