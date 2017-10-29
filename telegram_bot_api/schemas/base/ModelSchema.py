from marshmallow import post_load


class ModelSchema:
    def __init__(self):
        self.__model__ = None

    @post_load
    def make_model(self, data):
        model = self.__import_model()

        return model(**data)

    def __import_model(self):
        model = __import__('telegram_bot_api.models.%s' % self.__model__, fromlist=self.__model__)

        return getattr(model, self.__model__)
