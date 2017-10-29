from marshmallow import Schema, fields
from .base.ModelSchema import ModelSchema


class MessageSchema(Schema, ModelSchema):
    __model__ = 'Message'

    message_id = fields.Int(required=True)
    from_user = fields.Nested('UserSchema', load_from='from')
    date = fields.Int(required=True)
    chat = fields.Nested('ChatSchema', required=True)
    forward_from = fields.Nested('UserSchema')
    forward_from_chat = fields.Nested('ChatSchema')
    forward_from_message_id = fields.Int()
    forward_signature = fields.Str()
    forward_date = fields.Int()
    reply_to_message = fields.Nested('self')
    edit_date = fields.Int()
    author_signature = fields.Str()
    text = fields.Str()
    entities = fields.Nested('MessageEntitySchema', many=True)
    caption_entities = fields.Nested('MessageEntitySchema', many=True)
    audio = fields.Nested('AudioSchema')
    document = fields.Nested('DocumentSchema')
    game = fields.Nested('GameSchema')
    photo = fields.Nested('PhotoSizeSchema', many=True)
    sticker = fields.Nested('StickerSchema')
    video = fields.Nested('VideoSchema')
    voice = fields.Nested('VoiceSchema')
    video_note = fields.Nested('VideoNoteSchema')
    caption = fields.Str()
    contact = fields.Nested('ContactSchema')
    location = fields.Nested('LocationSchema')
    venue = fields.Nested('VenueSchema')
    new_chat_members = fields.Nested('UserSchema', many=True)
    left_chat_member = fields.Nested('UserSchema')
    new_chat_title = fields.Str()
    new_chat_photo = fields.Nested('PhotoSizeSchema', many=True)
    delete_chat_photo = fields.Bool()
    group_chat_created = fields.Bool()
    supergroup_chat_created = fields.Bool()
    channel_chat_created = fields.Bool()
    migrate_to_chat_id = fields.Int()
    migrate_from_chat_id = fields.Int()
    pinned_message = fields.Nested('self')
    invoice = fields.Nested('InvoiceSchema')
    successful_payment = fields.Nested('SuccessfulPaymentSchema')
