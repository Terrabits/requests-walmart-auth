from .helpers import new_keys
from pathlib  import Path


def generate_keys(secrets_path, passphrase=None):
    # is valid secrets path?
    secrets_path = Path(secrets_path)
    if not secrets_path.exists():
        raise ValueError(f"error: path '{secrets_path}' does not exist")
    if not secrets_path.is_dir():
        raise ValueError(f"error: path '{secrets_path}' is not a directory")

    # get key file paths
    public_key_file     = secrets_path / 'public_key.pem'
    public_key_b64_file = secrets_path / 'public_key.b64.txt'
    private_key_file    = secrets_path / 'private_key.pem'

    # generate new keys
    public_key, private_key = new_keys(passphrase)

    # save .pem files
    with public_key_file.open('wb') as f:
        f.write(public_key)
    with private_key_file.open('wb') as f:
        f.write(private_key)

    # save public_key.b64.txt
    public_key_b64 = public_key.lstrip(b'-----BEGIN PUBLIC KEY-----\n')
    public_key_b64 = public_key_b64.rstrip(b'-----END PUBLIC KEY-----\n')
    with public_key_b64_file.open('wb') as f:
        f.write(public_key_b64)
