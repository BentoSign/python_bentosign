from bentosign import BentoObject

class Package(BentoObject):
    @classmethod
    def get_class_url(cls):
        url = cls.get_base_url()+'packages'
        return url

    @classmethod
    def create(cls, api_key=None, idempotency_key=None,
               stripe_version=None, stripe_account=None, **params):
        requestor = api_requestor.APIRequestor(api_key,
                                               api_version=stripe_version,
                                               account=stripe_account)
        url = cls.class_url()
        headers = util.populate_headers(idempotency_key)
        response, api_key = requestor.request('post', url, params, headers)

        return util.convert_to_stripe_object(response, api_key, stripe_version,
                                             stripe_account)
