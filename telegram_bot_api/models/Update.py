if False:
    from .Message import Message


class Update:
    def __init__(self, update_id: int,
                 message: 'Message'=None,
                 edited_message: 'Message'=None,
                 channel_post: 'Message'=None,
                 edited_channel_post: 'Message'=None,
                 inline_query=None,
                 chosen_inline_result=None,
                 callback_query=None,
                 shipping_query=None,
                 pre_checkout_query=None):
        self.id = update_id
        self.message = message
        self.edited_message = edited_message
        self.channel_post = channel_post
        self.edited_channel_post = edited_channel_post
        self.inline_query = inline_query
        self.chosen_inline_result = chosen_inline_result
        self.callback_query = callback_query
        self.shipping_query = shipping_query
        self.pre_checkout_query = pre_checkout_query

    def __repr__(self):
        return '<%s(id=%d)>' % (
            self.__class__.__name__,
            self.id
        )
