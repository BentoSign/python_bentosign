from bentosign import BentoSignObject, BentoSignError

class Recipient(BentoSignObject):
    @classmethod
    def get_class_url(cls):
        url = cls.get_base_url()+'recipients'
        return url

    @classmethod
    def get_or_create(cls, email, api_key=None, **params):
        object = cls(email, api_key, **params)
        try:
            object.get_object()
        except BentoSignError:
            pass
        return object
