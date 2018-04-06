from bentosign import BentoObject

class Document(BentoObject):
    @classmethod
    def get_class_url(cls):
        url = cls.get_base_url()+'documents'
        return url
