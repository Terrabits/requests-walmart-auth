from   .fixtures import SECRETS
from   .mock     import use_mock_cache_timer
import unittest
from   walmart_auth.signed_headers_factory import SignedHeadersFactory


class TestSignedHeadersFactory(unittest.TestCase):
    def test_signature(self):
        # get signature at known timestamp
        use_mock_cache_timer(time_ms=1234567890123)
        factory   = SignedHeadersFactory(**SECRETS)
        headers   = factory.get_headers()
        signature_b64 = headers['WM_SEC.AUTH_SIGNATURE']

        # generated from java reference code
        expected_b64  = 'ZaN1kLdbDPnrITndhHN3AQiNg2WsAlJES0UEqKvyug0mjr3obrpXV6V37sZDgSm91lsX88pq2QIoMHao/kTMLt1jkHQOAjS6cbNRfoq3nLCaUAyXyWc/ynDAHHd6pVcgumjA9VmV1gccQqti+wTQkSg9IWR9+k0NIenwlHYoTRcWrN3MoqyBG2eEU49Vlu7AEJRYEVtNiOrZBdPOmdEf9paXx2h+bB1qeQiMTX7henOc1dorLiDx4jwMoOu1ef1I5Zm4nNspLRBhi0abOAWiAPy+cWiGl7tPdzdogdEZcnbWd0Jf4D+HMVak8ci6hHECwThSsguIhcJ6vS2xfyHLgQ=='

        # python code should match reference code
        self.assertEqual(signature_b64, expected_b64)
