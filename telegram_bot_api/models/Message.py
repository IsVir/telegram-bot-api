from telegram_bot_api.models.MessageEntity import MessageEntity

if False:
    from typing import List
    from telegram_bot_api.models.Chat import Chat
    from telegram_bot_api.models.User import User


class Message:
    def __init__(self, message_id: int,
                 from_user: 'User',
                 date: int,
                 chat: 'Chat',
                 forward_from: 'User'=None,
                 forward_from_chat=None,
                 forward_from_message_id: int=None,
                 forward_signature: str=None,
                 forward_date: int=None,
                 reply_to_message: 'Message'=None,
                 edit_date: int=None,
                 author_signature: str=None,
                 text: str=None,
                 entities: 'List[MessageEntity]'=[],
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

        self.__prepare_builtin_entities__()

    def get_text(self) -> str:
        """
        Use this method to get message text

        :return: message text
        """
        return self.text if self.text is not None else ''

    def has_commands(self) -> bool:
        """
        Use this method to find out if there is a commands in the message

        :return: If has commands return True
        """
        return True if len(self.__commands__) > 0 else False

    def get_commands(self, limit: int=None) -> 'List[str]':
        """
        Use this method to get commands from message

        :param limit: Limit of commands to return (default: unlimited)
        :return: List of commands or empty list
        """
        return self.__get_textual_entities__(self.__commands__, limit)

    def has_hashtags(self) -> bool:
        """
        Use this method to find out if there is a hashtags in the message

        :return: If has hashtags return True
        """
        return True if len(self.__hashtags__) > 0 else False

    def get_hashtags(self, limit: int=None) -> 'List[str]':
        """
        Use this method to get hashtags from message

        :param limit: Limit of hashtags to return (default: unlimited)
        :return: List of hashtags or empty list
        """
        return self.__get_textual_entities__(self.__hashtags__, limit)

    def has_urls(self) -> bool:
        """
        Use this method to find out if there is a urls in the message

        :return: If has urls return True
        """
        return True if len(self.__urls__) > 0 else False

    def get_urls(self, limit: int=None) -> 'List[str]':
        """
        Use this method to get urls from message

        :param limit: Limit of urls to return (default: unlimited)
        :return: List of urls or empty list
        """
        return self.__get_textual_entities__(self.__urls__, limit)
    
    def has_emails(self) -> bool:
        """
        Use this method to find out if there is a emails in the message

        :return: If has emails return True
        """
        return True if len(self.__emails__) > 0 else False

    def get_emails(self, limit: int=None) -> 'List[str]':
        """
        Use this method to get emails from message

        :param limit: Limit of emails to return (default: unlimited)
        :return: List of emails or empty list
        """
        return self.__get_textual_entities__(self.__emails__, limit)
    
    def has_bold_text(self) -> bool:
        """
        Use this method to find out if there is a bold text in the message

        :return: If has bold text return True
        """
        return True if len(self.__bold_text__) > 0 else False

    def get_bold_text(self, limit: int=None) -> 'List[str]':
        """
        Use this method to get bold text from message

        :param limit: Limit of bold text to return (default: unlimited)
        :return: List of bold text or empty list
        """
        return self.__get_textual_entities__(self.__bold_text__, limit)

    def has_italice_text(self) -> bool:
        """
        Use this method to find out if there is a italice text in the message

        :return: If has italice text return True
        """
        return True if len(self.__italice_text__) > 0 else False

    def get_italice_text(self, limit: int=None) -> 'List[str]':
        """
        Use this method to get italice text from message

        :param limit: Limit of italice text to return (default: unlimited)
        :return: List of italice text or empty list
        """
        return self.__get_textual_entities__(self.__italice_text__, limit)
    
    def has_code_blocks(self) -> bool:
        """
        Use this method to find out if there is a code blocks in the message

        :return: If has code blocks return True
        """
        return True if len(self.__code_blocks__) > 0 else False

    def get_code_blocks(self, limit: int=None) -> 'List[str]':
        """
        Use this method to get code blocks from message

        :param limit: Limit of code blocks to return (default: unlimited)
        :return: List of code blocks or empty list
        """
        return self.__get_textual_entities__(self.__code_blocks__, limit)

    def has_pre_blocks(self) -> bool:
        """
        Use this method to find out if there is a pre blocks in the message

        :return: If has pre blocks return True
        """
        return True if len(self.__pre_blocks__) > 0 else False

    def get_pre_blocks(self, limit: int=None) -> 'List[str]':
        """
        Use this method to get pre blocks from message

        :param limit: Limit of pre blocks to return (default: unlimited)
        :return: List of pre blocks or empty list
        """
        return self.__get_textual_entities__(self.__pre_blocks__, limit)
    
    def has_text_links(self) -> bool:
        """
        Use this method to find out if there is a text links in the message

        :return: If has text links return True
        """
        return True if len(self.__text_links__) > 0 else False

    def get_text_links(self, limit: int=None) -> 'List[str]':
        """
        Use this method to get text links from message

        :param limit: Limit of text links to return (default: unlimited)
        :return: List of text links or empty list
        """
        return self.__get_textual_entities__(self.__text_links__, limit)

    def has_text_mentions(self) -> bool:
        """
        Use this method to find out if there is a text mentions in the message

        :return: If has text mentions return True
        """
        return True if len(self.__text_mentions__) > 0 else False

    def get_text_mentions(self, limit: int=None) -> 'List[str]':
        """
        Use this method to get text mentions from message

        :param limit: Limit of text mentions to return (default: unlimited)
        :return: List of text mentions or empty list
        """
        return self.__get_textual_entities__(self.__text_mentions__, limit)

    def __get_textual_entities__(self, entities: 'List[MessageEntity]', limit: int= None) -> 'List[str]':
        textual_entities = []

        for entity in entities:
            if limit is not None:
                if limit > 0:
                    limit -= 1
                else:
                    break

            textual_entities.append(self.text[entity.offset:entity.offset+entity.length])

        return textual_entities

    def __prepare_builtin_entities__(self):
        self.__commands__ = []
        self.__hashtags__ = []
        self.__urls__ = []
        self.__emails__ = []
        self.__bold_text__ = []
        self.__italice_text__ = []
        self.__code_blocks__ = []
        self.__pre_blocks__ = []
        self.__text_links__ = []
        self.__text_mentions__ = []

        for entity in self.entities:
            if entity.is_type(MessageEntity.AVAILABLE_TYPES['COMMAND']):
                self.__commands__.append(entity)
            elif entity.is_type(MessageEntity.AVAILABLE_TYPES['HASHTAG']):
                self.__hashtags__.append(entity)
            elif entity.is_type(MessageEntity.AVAILABLE_TYPES['URL']):
                self.__urls__.append(entity)
            elif entity.is_type(MessageEntity.AVAILABLE_TYPES['EMAIL']):
                self.__emails__.append(entity)
            elif entity.is_type(MessageEntity.AVAILABLE_TYPES['BOLD']):
                self.__bold_text__.append(entity)
            elif entity.is_type(MessageEntity.AVAILABLE_TYPES['ITALICE']):
                self.__italice_text__.append(entity)
            elif entity.is_type(MessageEntity.AVAILABLE_TYPES['CODE']):
                self.__code_blocks__.append(entity)
            elif entity.is_type(MessageEntity.AVAILABLE_TYPES['PRE']):
                self.__pre_blocks__.append(entity)
            elif entity.is_type(MessageEntity.AVAILABLE_TYPES['TEXT_LINK']):
                self.__text_links__.append(entity)
            elif entity.is_type(MessageEntity.AVAILABLE_TYPES['TEXT_MENTIONS']):
                self.__text_mentions__.append(entity)

    def __repr__(self):
        return '<%s(id=%d)>' % (
            self.__class__.__name__,
            self.id
        )
