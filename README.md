# telegram-bot-api
Module for working with Telegram Bot API

## Available methods

**get_updates**
>"""
>Use this method to receive incoming updates
>
>:param offset: Identifier of the first update to be returned.
>:param limit: Limits the number of updates to be retrieved. Values between 1—100 are accepted. Defaults to 100.
>:param timeout: Timeout in seconds for long polling. Defaults to 0, i.e. usual short polling.
>:param allowed_updates: List the types of updates you want your bot to receive. For example, specify [“message”,
>    “edited_channel_post”, “callback_query”] to only receive updates of these types.
>:return:
>"""

**get_me**
**send_message**
**send_photo**
**send_audio**
**forward_message**