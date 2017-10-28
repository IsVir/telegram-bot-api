import mimetypes
import requests
from random import randint
from time import time
from typing import Union
from marshmallow import Schema, MarshalResult

from .schemas.ErrorSchema import ErrorSchema
from .schemas.MessageSchema import MessageSchema
from .schemas.UpdateSchema import UpdateSchema
from .schemas.UserSchema import UserSchema
from .schemas.WebhookSchema import WebhookSchema


class TelegramBotApi:
    API_URL_PART = 'https://api.telegram.org/bot'
    API_FILE_URL_PART = 'https://api.telegram.org/file/bot'

    def __init__(self, access_token: str):
        self.__access_token = access_token

    def get_updates(self, offset: int=0, limit: int=100, timeout: int=0, allowed_updates: list=list()) -> list:
        """
        Use this method to receive incoming updates

        :param offset: Identifier of the first update to be returned.
        :param limit: Limits the number of updates to be retrieved. Values between 1—100 are accepted. Defaults to 100.
        :param timeout: Timeout in seconds for long polling. Defaults to 0, i.e. usual short polling.
        :param allowed_updates: List the types of updates you want your bot to receive. For example, specify [“message”,
            “edited_channel_post”, “callback_query”] to only receive updates of these types.
        :return: list of updates
        """
        url = self.__get_api_url('getUpdates')
        data = {
            'offset': offset,
            'limit': limit,
            'timeout': timeout,
            'allowed_updates': allowed_updates
        }

        result = self.__request(url, data, UpdateSchema(many=True))

        return result.data

    def set_webhook(self, webhook_url: str,
                    certificate: str = None,
                    max_connections: int = 40,
                    allowed_updates: list = None):
        """
        Use this method to specify a url and receive incoming updates via an outgoing webhook.

        :param webhook_url: HTTPS url to send updates to. Use an empty string to remove webhook integration
        :param certificate: Upload your public key certificate so that the root certificate in use can be checked.
        :param max_connections: Maximum allowed number of simultaneous HTTPS connections to the webhook for update
            delivery, 1-100. Defaults to 40. Use lower values to limit the load on your bot‘s server, and higher values
            to increase your bot’s throughput.
        :param allowed_updates: List the types of updates you want your bot to receive. For example, specify
            [“message”, “edited_channel_post”, “callback_query”] to only receive updates of these types.
        :return: dict
        """
        url = self.__get_api_url('setWebhook')
        data = {
            'url': webhook_url,
            'max_connections': max_connections,
        }

        if isinstance(allowed_updates, list) and len(allowed_updates) > 0:
            data['allowed_updates'] = allowed_updates

        if certificate is not None:
            raise NotImplementedError('Working with certificate not implemented yer')

        result = self.__request(url, data, WebhookSchema(), raw=True)

        return result.data

    def delete_webhook(self):
        """
        Use this method to delete previously mentioned webhook
        :return:
        """
        return self.set_webhook('')

    def get_me(self) -> dict:
        """
        A simple method for testing your bot's auth token.
        :return: dict
        """
        url = self.__get_api_url('getMe')
        result = self.__request(url, {}, UserSchema())

        return result.data

    def send_message(self, chat_id: Union[int, str],
                     text: str,
                     parse_mode: Union[str, None] = None,
                     disable_web_page_preview: bool = False,
                     disable_notification: bool = False,
                     reply_to_message_id: int = None,
                     reply_markup: str = None) -> dict:
        """
        Use this method to send text messages.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format
            @channelusername)
        :param text: Text of the message to be sent.
        :param parse_mode: Set Markdown or HTML.
        :param disable_web_page_preview: Disables link previews for links in this message.
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :param reply_to_message_id: If the message is a reply, ID of the original message.
        :param reply_markup: Additional interface options.
        :return: dict
        """
        url = self.__get_api_url('sendMessage')
        data = {
            'chat_id': chat_id,
            'text': text,
            'disable_web_page_preview': disable_web_page_preview,
            'disable_notification': disable_notification,
        }

        if parse_mode is not None and parse_mode not in ['Markdown', 'HTML']:
            raise ValueError('parse_mode must be "Markdown" or "HTML"')
        elif parse_mode is not None:
            data['parse_mode'] = parse_mode

        if reply_to_message_id is not None:
            data['reply_to_message_id'] = reply_to_message_id

        if reply_markup is not None:
            data['reply_markup'] = reply_markup

        result = self.__request(url, data, MessageSchema())

        return result.data

    def send_photo(self, chat_id: Union[int, str],
                   photo: Union[int, str],
                   caption: str = None,
                   disable_notification: bool = False,
                   reply_to_message_id: int = None,
                   reply_markup: dict = None) -> dict:
        """
        Use this method to send photos.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format
            @channelusername)
        :param photo: Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers
            (recommended), pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new
            photo by passing full path to file as a String
        :param caption: Photo caption (may also be used when resending photos by file_id), 0-200 characters
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :param reply_to_message_id: If the message is a reply, ID of the original message.
        :param reply_markup: Additional interface options.
        :return: dict
        """
        url = self.__get_api_url('sendPhoto')
        data = {
            'chat_id': chat_id,
            'disable_notification': disable_notification,
        }
        kwargs = {}

        try:
            upload_method = self.__detect_file_upload_method(photo)
        except FileNotFoundError:
            return {'error_code': -1, 'description': 'File not found'}

        if 'file' in upload_method:
            kwargs['files'] = {'photo': upload_method['file']}
        else:
            data['photo'] = upload_method['string']

        if caption is not None:
            data['caption'] = caption[0:200]

        if reply_to_message_id is not None:
            data['reply_to_message_id'] = reply_to_message_id

        if reply_markup is not None:
            data['reply_markup'] = reply_markup

        result = self.__request(url, data, MessageSchema(), **kwargs)

        return result.data

    def send_audio(self, chat_id: Union[int, str],
                   audio: Union[int, str],
                   caption: str = None,
                   duration: int = None,
                   performer: str = None,
                   title: str = None,
                   disable_notification: bool = False,
                   reply_to_message_id: int = None,
                   reply_markup: dict = None) -> dict:
        """
        Use this method to send audio files, if you want Telegram clients to display them in the music player. Your
        audio must be in the .mp3 format. Bots can currently send audio files of up to 50 MB in size

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format
            @channelusername)
        :param audio: Audio file to send. Pass a file_id as String to send a audio file that exists on the Telegram
            servers (recommended), pass an HTTP URL as a String for Telegram to get a audio file from the Internet, or
            upload a new audio file by passing full path to file as a String
        :param caption: Audio caption (may also be used when resending photos by file_id), 0-200 characters
        :param duration: Duration of the audio in seconds.
        :param performer: Performer
        :param title: Track name
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :param reply_to_message_id: If the message is a reply, ID of the original message.
        :param reply_markup: Additional interface options.
        :return: dict
        """
        url = self.__get_api_url('sendAudio')
        data = {
            'chat_id': chat_id,
            'disable_notification': disable_notification,
        }
        kwargs = {}

        try:
            upload_method = self.__detect_file_upload_method(audio)
        except FileNotFoundError:
            return {'error_code': -1, 'description': 'File not found'}

        if 'file' in upload_method:
            kwargs['files'] = {'audio': upload_method['file']}
        else:
            data['audio'] = upload_method['string']

        if caption is not None:
            data['caption'] = caption[0:200]

        if duration is not None:
            data['duration'] = duration

        if performer is not None:
            data['performer'] = performer

        if title is not None:
            data['title'] = title

        if reply_to_message_id is not None:
            data['reply_to_message_id'] = reply_to_message_id

        if reply_markup is not None:
            data['reply_markup'] = reply_markup

        result = self.__request(url, data, MessageSchema(), **kwargs)

        return result.data

    def forward_message(self, chat_id: Union[int, str],
                        from_chat_id: Union[int, str],
                        message_id: int,
                        disable_notification: bool = False) -> dict:
        """
        Use this method to forward messages of any kind.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format
            @channelusername)
        :param from_chat_id: Unique identifier for the chat where the original message was sent (or channel username in
            the format @channelusername)
        :param message_id: Message identifier in the chat specified in from_chat_id
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :return: dict
        """
        url = self.__get_api_url('forwardMessage')
        data = {
            'chat_id': chat_id,
            'from_chat_id': from_chat_id,
            'message_id': message_id,
            'disable_notifications': disable_notification
        }

        result = self.__request(url, data, MessageSchema())

        return result.data

    def get_file_url(self, file_path: str) -> str:
        """
        Use this method to get full path url to file
        """
        return '%s%s/%s' % (TelegramBotApi.API_FILE_URL_PART, self.__access_token, file_path)

    @staticmethod
    def __request(url: str, data: dict, schema: Schema, files: dict = None, raw: bool = False) -> MarshalResult:
        """
        :raise RequestFiledException: If has no 'ok' field in response, or status code != 200
        """
        if files is None:
            files = dict()

        response = requests.post(
            url,
            data=data,
            files=files
        )
        # @TODO: Обязательно исправить это говно
        marshal_result = {'data': {}}

        if response.status_code == 200:
            data = response.json()

            if 'ok' in data and data['ok'] is True:
                if raw is True:
                    result = data
                else:
                    result = data['result']

                marshal_result = schema.load(result)
        else:
            data = response.json()

            if 'ok' in data and data['ok'] is False:
                schema = ErrorSchema()
                marshal_result = schema.load(data)

        return marshal_result

    @staticmethod
    def __detect_file_upload_method(file: str):
        result = {}

        if isinstance(file, str) and file[0:4] != 'http' and file.find('/') >= 0:
            f = open(file, 'rb')
            file_type = mimetypes.guess_type(f.name)[0]
            file_extension = mimetypes.guess_extension(file_type)

            result['file'] = ('%s_%s.%s' % (time(), randint(1, 100), file_extension), f, file_type)
        else:
            result['string'] = file

        return result

    def __get_api_url(self, method_name: str) -> str:
        return '%s%s/%s' % (TelegramBotApi.API_URL_PART, self.__access_token, method_name)
