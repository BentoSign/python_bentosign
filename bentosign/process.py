from bentosign import BentoSignObject

class Process(BentoSignObject):
    @classmethod
    def get_class_url(cls):
        url = cls.get_base_url()+'processes'
        return url

