from time import time


class CacheTimer:
    @staticmethod
    def time_since_epoch_s():
        return time()

    def __init__(self, expires_in_s):
        self.expires_in_s = expires_in_s
        self.last_time_s  = None

    @property
    def is_valid(self):
        if self.last_time_s is None:
            return False
        # else
        return CacheTimer.time_since_epoch_s() <= self.expires_at_s

    @property
    def expires_at_s(self):
        return self.last_time_s + self.expires_in_s

    def new_timestamp_str(self):
        """returns str containing (rounded) time in milliseconds since epoch"""
        self.last_time_s = CacheTimer.time_since_epoch_s()
        return str(round(self.last_time_s * 1000))
