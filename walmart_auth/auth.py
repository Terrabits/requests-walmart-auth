from .signed_headers_factory import SignedHeadersFactory
from requests.auth           import AuthBase


class WalmartAuth(AuthBase):
    def __init__(self, consumer_id, private_key, key_version, passphrase=None):
        self.factory = SignedHeadersFactory(consumer_id, private_key, key_version, passphrase=None)

    def __call__(self, request):
        signed_headers = self.factory.get_headers()
        # import pdb; pdb.set_trace()
        request.headers.update(signed_headers)
        return request
