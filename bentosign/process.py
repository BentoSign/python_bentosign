from bentosign import BentoObject

class Process(BentoObject):
    @classmethod
    def get_class_url(cls):
        url = cls.get_base_url()+'processes'
        return url

