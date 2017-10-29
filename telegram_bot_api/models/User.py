class User:
    def __init__(self, id: int,
                 is_bot: bool,
                 first_name: str,
                 last_name: str=None,
                 username: str=None,
                 language_code: str=None):
        self.id = id
        self.is_bot = is_bot
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.language_code = language_code

    def __repr__(self):
        return '<%s(id=%d)>' % (
            self.__class__.__name__,
            self.id
        )
