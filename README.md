# telegram-bot-api
Module for working with Telegram Bot API

## Available methods

**get_updates** - use this method to receive incoming updates.
>:param offset: Identifier of the first update to be returned.<br />
>:param limit: Limits the number of updates to be retrieved. Values between 1—100 are accepted. Defaults to 100.<br />
>:param timeout: Timeout in seconds for long polling. Defaults to 0, i.e. usual short polling.<br />
>:param allowed_updates: List the types of updates you want your bot to receive. For example, specify [“message”, “edited_channel_post”, “callback_query”] to only receive updates of these types.<br />
>:return: list of updates

**get_me**
**send_message**
**send_photo**
**send_audio**
**forward_message**