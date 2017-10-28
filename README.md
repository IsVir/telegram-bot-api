# telegram-bot-api
Module for working with Telegram Bot API

## Simple code
```python
from telegram-bot-api.api import TelegramBotApi

api = TelegramBotApi('bot-access-token-here')
updates = api.get_updates()

for update in updates:
    print(update)
```

Result:
```python
{'text': 'Hi!', 'chat': {'first_name': 'Bob', 'id': 62490, 'last_name': 'Smith', 'username': 'BobSmith', 'type': 'private'}, 'date': 1509095664, 'message_id': 7}
```

## Available methods

**get_updates** - use this method to receive incoming updates.
>:param offset: Identifier of the first update to be returned.<br />
:param limit: Limits the number of updates to be retrieved. Values between 1—100 are accepted. Defaults to 100.<br />
:param timeout: Timeout in seconds for long polling. Defaults to 0, i.e. usual short polling.<br />
:param allowed_updates: List the types of updates you want your bot to receive. For example, specify [“message”, “edited_channel_post”, “callback_query”] to only receive updates of these types.<br />
:return: list of updates

**get_me** - a simple method for testing your bot's auth token.
>:return: dict

**send_message** - use this method to send text messages.
>:param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)<br />
:param text: Text of the message to be sent.<br />
:param parse_mode: Set Markdown or HTML.<br />
:param disable_web_page_preview: Disables link previews for links in this message.<br />
:param disable_notification: Sends the message silently. Users will receive a notification with no sound.<br />
:param reply_to_message_id: If the message is a reply, ID of the original message.<br />
:param reply_markup: Additional interface options.<br />
:return: dict<br />

**send_photo** - use this method to send photos.
>:param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)<br />
:param photo: Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo by passing full path to file as a String<br />
:param caption: Photo caption (may also be used when resending photos by file_id), 0-200 characters<br />
:param disable_notification: Sends the message silently. Users will receive a notification with no sound.<br />
:param reply_to_message_id: If the message is a reply, ID of the original message.<br />
:param reply_markup: Additional interface options.<br />
:return: dict

**send_audio** - use this method to send audio files, if you want Telegram clients to display them in the music player. Your audio must be in the .mp3 format. Bots can currently send audio files of up to 50 MB in size
>:param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)<br />
:param audio: Audio file to send. Pass a file_id as String to send a audio file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a audio file from the Internet, or upload a new audio file by passing full path to file as a String<br />
:param caption: Audio caption (may also be used when resending photos by file_id), 0-200 characters<br />
:param duration: Duration of the audio in seconds.<br />
:param performer: Performer<br />
:param title: Track name<br />
:param disable_notification: Sends the message silently. Users will receive a notification with no sound.<br />
:param reply_to_message_id: If the message is a reply, ID of the original message.<br />
:param reply_markup: Additional interface options.<br />
:return: dict 

**forward_message** - use this method to forward messages of any kind.
>:param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)<br />
:param from_chat_id: Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername)<br />
:param message_id: Message identifier in the chat specified in from_chat_id<br />
:param disable_notification: Sends the message silently. Users will receive a notification with no sound.<br />
:return: dict

