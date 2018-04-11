import json
import requests

from .bento_errors import BentoError

# An BentoObject is a dictionary where ``object.key=value`` is a shortcut for ``object[key]=value``
class BentoObject(dict):

    def __init__(self):
        super(BentoObject, self).__init__()


    # Define __getattr__, __setattr__ and __delattr, so that
    # object.name becomes an alias to object['name']
    def __getattr__(self, key):
        if key[0] == '_':
            raise AttributeError('No such attribute: ' + key)
        if key in self:
            return self[key]
        else:
            raise AttributeError('No such attribute: ' + key)

    def __setattr__(self, key, value):
        if key[0] == '_':
            return super(BentoObject, self).__setattr__(key, value)
        self[key] = value

    def __delattr__(self, key):
        if key[0] == '_':
            return super(BentoObject, self).__delattr__(key)
        if key in self:
            del self[key]
        else:
            raise AttributeError('No such attribute: ' + key)
    # Define __getattr__, __setattr__ and __delattr, so that
    # object.name becomes an alias to object['name']


    @classmethod
    def get_base_url(cls):
        return 'http://localhost:5000/api/v1.0/'

    @classmethod
    def get_class_url(cls):
        raise NotImplementedError()

    @classmethod
    def get(cls, id):
        # Perform an HTTP GET
        url = cls.get_class_url() + '/' + id
        response = requests.get(url)
        cls._process_response_code('GET', url, response)

        # Create Object from JSON
        object = cls()
        data = json.loads(response.content)
        object.load_object_from_data(data)
        return object

    @classmethod
    def find(cls, **params):
        # Perform an HTTP GET with params
        url = cls.get_class_url()
        response = requests.get(url, params=params)
        cls._process_response_code('GET', url, response)

        # Create Objects from JSON list
        objects = []
        data_list = json.loads(response.content)
        for data in data_list:
            object = cls()
            object.load_object_from_data(data)
            objects.append(object)

        return objects

    @classmethod
    def create(cls, **params):
        # Perform an HTTP POST
        url = cls.get_class_url()
        response = requests.post(url, data=params)
        cls._process_response_code('POST', url, response)

        # Create Object from JSON
        object = cls()
        data = json.loads(response.content)
        object.load_object_from_data(data)
        return object

    @classmethod
    def delete(cls, id):
        # Perform an HTTP DELETE
        url = cls.get_class_url() + '/' + id
        response = requests.delete(url)
        cls._process_response_code('DELETE', url, response)

    def load_object_from_data(self, data):
        for key, value in data.items():
            self[key] = value

    @classmethod
    def _process_response_code(cls, method, url, response):
        if response.status_code!=200:
            raise BentoError(method + ' ' + url + ' returned ' + str(response.status_code))
