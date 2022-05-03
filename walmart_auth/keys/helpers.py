from Crypto.PublicKey import RSA


# constants
BITS = 2048


def new_keys(passphrase=None):
    keys        = RSA.generate(BITS)
    public_key  = keys.publickey().export_key()
    private_key = keys.export_key(passphrase=passphrase, pkcs=8)
    return public_key, private_key
