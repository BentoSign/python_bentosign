from bentosign import BentoSignObject

class Document(BentoSignObject):
    @classmethod
    def get_class_url(cls):
        url = cls.get_base_url()+'documents'
        return url
