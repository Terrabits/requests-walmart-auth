from .cache_timer import CacheTimer
from .helpers     import to_bytes
from .sign        import sign


# constants
HEADER_VALID_FOR_S = 180
WIGGLE_ROOM_S      = 5
HEADER_LIFETIME_S  = HEADER_VALID_FOR_S - WIGGLE_ROOM_S


class SignedHeadersFactory:
    def __init__(self, consumer_id, private_key, key_version, passphrase=None):
        # client info
        self.consumer_id = consumer_id
        self.private_key = private_key
        self.key_version = key_version
        self.passphrase  = passphrase

        # lifecycle
        self.last_header = None
        self.cache_timer = CacheTimer(expires_in_s=HEADER_LIFETIME_S)

    def get_headers(self):
        if not self.cache_timer.is_valid:
            self.last_header = self.new_header()
        return self.last_header

    # helpers

    def new_header(self):
        # new header
        headers = {
            'WM_CONSUMER.ID':          self.consumer_id,
            'WM_SEC.KEY_VERSION':      self.key_version,
            'WM_CONSUMER.INTIMESTAMP': self.cache_timer.new_timestamp_str()
        }

        # sign
        data      = to_bytes(headers)
        signature = sign(self.private_key, data, self.passphrase)
        headers['WM_SEC.AUTH_SIGNATURE'] = signature
        return headers
