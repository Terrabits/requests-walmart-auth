from pathlib import Path


# paths
fixtures_path = Path(__file__).parent.resolve()
private_key   = fixtures_path / 'private_key.pem'


with private_key.open() as f:
    SECRETS = {
        'consumer_id': '12345678-1234-1234-1234-123456789012',
        'private_key': f.read(),
        'key_version': '1'
    }
