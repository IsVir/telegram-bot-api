class MessageEntity:
    AVAILABLE_TYPES = {
        'COMMAND': 'bot_command',
        'HASHTAG': 'hashtag',
        'URL': 'url',
        'EMAIL': 'email',
        'BOLD': 'bold',
        'ITALICE': 'italic',
        'CODE': 'code',
        'PRE': 'pre',
        'TEXT_LINK': 'text_link',
        'TEXT_MENTIONS': 'text_mention',
    }

    def __init__(self, type,
                 offset,
                 length,
                 url=None,
                 user=None):
        self.type = type
        self.offset = offset
        self.length = length
        self.url = url
        self.user = user

    def is_type(self, type):
        return True if self.type == type else False

    def __repr__(self):
        return '<%s(%s)>' % (
            self.__class__.__name__,
            self.type
        )
