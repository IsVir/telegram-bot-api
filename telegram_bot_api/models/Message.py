from telegram_bot_api.models.User import User


class Message:
    def __init__(self, message_id: int,
                 from_user: User,
                 date: int,
                 chat,
                 forward_from: User=None,
                 forward_from_chat=None,
                 forward_from_message_id: int=None,
                 forward_signature: str=None,
                 forward_date: int=None,
                 # @TODO: Что делать с типом?
                 reply_to_message=None,
                 edit_date: int=None,
                 author_signature: str=None,
                 text: str=None,
                 entities=None,
                 caption_entities=None,
                 audio=None,
                 document=None,
                 game=None,
                 photo=None,
                 sticker=None,
                 video=None,
                 voice=None,
                 video_note=None,
                 caption: str=None,
                 contact=None,
                 location=None,
                 venue=None,
                 new_chat_members=None,
                 left_chat_member=None,
                 new_chat_title: str=None,
                 new_chat_photo=None,
                 delete_chat_photo: bool=None,
                 group_chat_created: bool=None,
                 supergroup_chat_created: bool=None,
                 channel_chat_created: bool=None,
                 migrate_to_chat_id:int =None,
                 migrate_from_chat_id: int=None,
                 pinned_message=None,
                 invoice=None,
                 successful_payment=None):
        self.id = message_id
        self.from_user = from_user
        self.date = date
        self.chat = chat
        self.forward_from = forward_from
        self.forward_from_chat = forward_from_chat
        self.forward_from_message_id = forward_from_message_id
        self.forward_signature = forward_signature
        self.forward_date = forward_date
        self.reply_to_message = reply_to_message
        self.edit_date = edit_date
        self.author_signature = author_signature
        self.text = text
        self.entities = entities
        self.caption_entities = caption_entities
        self.audio = audio
        self.document = document
        self.game = game
        self.photo = photo
        self.sticker = sticker
        self.video = video
        self.voice = voice
        self.video_note = video_note
        self.caption = caption
        self.contact = contact
        self.location = location
        self.venue = venue
        self.new_chat_members = new_chat_members
        self.left_chat_member = left_chat_member
        self.new_chat_title = new_chat_title
        self.new_chat_photo = new_chat_photo
        self.delete_chat_photo = delete_chat_photo
        self.group_chat_created = group_chat_created
        self.supergroup_chat_created = supergroup_chat_created
        self.channel_chat_created = channel_chat_created
        self.migrate_to_chat_id = migrate_to_chat_id
        self.migrate_from_chat_id = migrate_from_chat_id
        self.pinned_message = pinned_message
        self.invoice = invoice
        self.successful_payment = successful_payment

    def __repr__(self):
        return '<%s(id=%d)>' % (
            self.__class__.__name__,
            self.id
        )
