from   .fixtures    import SECRETS
from   .mock        import MockRequest, use_mock_cache_timer
import unittest
from   walmart_auth import WalmartAuth, WalmartSession


class TestSession(unittest.TestCase):
    def test_session_auth_is_walmart_auth(self):
        session = WalmartSession(**SECRETS)

        # session auth should be
        # WalmartAuth instance
        self.assertIsInstance(session.auth, WalmartAuth)
