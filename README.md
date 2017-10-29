# Telegram Bot Api
Module for working with Telegram Bot API

!!! ATTENTION !!! Project in the active development stage, everything can change every day!

## Installation
```text
git clone https://github.com/IsVir/telegram-bot-api . 
```

## Simple code
```python
from telegram_bot_api.api import TelegramBotApi

api = TelegramBotApi('bot-access-token-here')
updates = api.get_updates()

for update in updates:
    print(update)
```

There is result:
```python
<Update(id=3245)>
```

## Available methods

**get_updates** - use this method to receive incoming updates.
```pydocstring
:param offset: Identifier of the first update to be returned.
:param limit: Limits the number of updates to be retrieved. Values between 1—100 are accepted. 
    Defaults to 100.
:param timeout: Timeout in seconds for long polling. Defaults to 0, i.e. usual short polling.
:param allowed_updates: List the types of updates you want your bot to receive. For example, 
    specify [“message”, “edited_channel_post”, “callback_query”] to only receive updates of these 
    types.
:return: list of Update objects
```

**set_webhook** - use this method to specify a url and receive incoming updates via an outgoing webhook.
```pydocstring
:param webhook_url: HTTPS url to send updates to. Use an empty string to remove webhook integration
:param certificate: Upload your public key certificate so that the root certificate in use can be checked.
:param max_connections: Maximum allowed number of simultaneous HTTPS connections to the webhook for update
    delivery, 1-100. Defaults to 40. Use lower values to limit the load on your bot‘s server, and higher values
    to increase your bot’s throughput.
:param allowed_updates: List the types of updates you want your bot to receive. For example, specify
    [“message”, “edited_channel_post”, “callback_query”] to only receive updates of these types.
:return: dict
```

**delete_webhook** - Use this method to delete previously mentioned webhook

**get_me** - a simple method for testing your bot's auth token.
```pydocstring
:return: dict
```

**send_message** - use this method to send text messages.
```pydocstring
:param chat_id: Unique identifier for the target chat or username of the target channel 
    (in the format @channelusername)
:param text: Text of the message to be sent.
:param parse_mode: Set Markdown or HTML.
:param disable_web_page_preview: Disables link previews for links in this message.
:param disable_notification: Sends the message silently. Users will receive a notification 
    with no sound.
:param reply_to_message_id: If the message is a reply, ID of the original message.
:param reply_markup: Additional interface options.
:return: Message
```

**send_photo** - use this method to send photos.
```pydocstring
:param chat_id: Unique identifier for the target chat or username of the target channel 
    (in the format @channelusername)
:param photo: Photo to send. Pass a file_id as String to send a photo that exists on 
    the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get 
    a photo from the Internet, or upload a new photo by passing full path to file as a String
:param caption: Photo caption (may also be used when resending photos by file_id), 0-200 characters
:param disable_notification: Sends the message silently. Users will receive a notification with no sound.
:param reply_to_message_id: If the message is a reply, ID of the original message.
:param reply_markup: Additional interface options.
:return: Message
```

**send_audio** - use this method to send audio files, if you want Telegram clients to display them in the music player. Your audio must be in the .mp3 format. Bots can currently send audio files of up to 50 MB in size
```pydocstring
:param chat_id: Unique identifier for the target chat or username of the target channel 
    (in the format @channelusername)
:param audio: Audio file to send. Pass a file_id as String to send a audio file that exists
    on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get 
    a audio file from the Internet, or upload a new audio file by passing full path to file
    as a String
:param caption: Audio caption (may also be used when resending photos by file_id), 0-200 characters
:param duration: Duration of the audio in seconds.
:param performer: Performer
:param title: Track name
:param disable_notification: Sends the message silently. Users will receive a notification with no sound.
:param reply_to_message_id: If the message is a reply, ID of the original message.
:param reply_markup: Additional interface options.
:return: Message
``` 

**forward_message** - use this method to forward messages of any kind.
```pydocstring
:param chat_id: Unique identifier for the target chat or username of the target channel 
    (in the format @channelusername)
:param from_chat_id: Unique identifier for the chat where the original message was sent 
    (or channel username in the format @channelusername)
:param message_id: Message identifier in the chat specified in from_chat_id
:param disable_notification: Sends the message silently. Users will receive a notification 
    with no sound.
:return: Message
```