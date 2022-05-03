def use_mock_cache_timer(time_ms):
    # monkeypatch MockCacheTimer
    # into SignedHeadersFactory() class module
    import walmart_auth.signed_headers_factory.signed_headers_factory as shf_module
    MockCacheTimer        = get_mock_cache_timer_class(time_ms)
    shf_module.CacheTimer = MockCacheTimer


def get_mock_cache_timer_class(time_ms):
    class MockCacheTimer:
        def __init__(self, *args, **kwargs):
            # ignore all args
            self.is_valid = False

        def new_timestamp_str(self):
            # unix time since epoch
            # units: ms
            # e.g. '1234567890123'
            return str(time_ms)
    return MockCacheTimer
