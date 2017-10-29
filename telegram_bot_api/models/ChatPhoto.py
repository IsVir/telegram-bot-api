class ChatPhoto:
    def __init__(self, small_file_id: str,
                 big_file_id: str):
        self.small_file_id = small_file_id
        self.big_file_id = big_file_id

    def __repr__(self):
        return '<%s>' % self.__class__.__name__
