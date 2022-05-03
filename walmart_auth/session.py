from .auth    import WalmartAuth
from requests import Session


class WalmartSession(Session):
    def __init__(self, consumer_id, private_key, key_version, passphrase=None):
        Session.__init__(self)
        self.auth = WalmartAuth(consumer_id, private_key, key_version, passphrase)
