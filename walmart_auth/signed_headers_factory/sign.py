from base64           import b64decode, b64encode
from Crypto.Hash      import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


def sign(private_key, data, passphrase=None):
    """return base64 hash (SHA256) and sign (PKCS1_v1_5) with private_key"""
    # hash, sign

    private_key = RSA.import_key(private_key, passphrase)
    signer    = PKCS1_v1_5.new(private_key)
    hasher    = SHA256.new(data)
    signature = signer.sign(hasher)

    # return as base64-encoded str
    return b64encode(signature).decode()
