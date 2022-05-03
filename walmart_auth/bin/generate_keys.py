from argparse     import ArgumentParser
from walmart_auth import generate_keys


def main():
    # command line interface (CLI)
    parser = ArgumentParser(description='generate keys for use with requests-walmart-auth')
    parser.add_argument('secrets_path')
    parser.add_argument('passphrase', nargs='?', default=None)

    # parse CLI
    args         = parser.parse_args()
    secrets_path = args.secrets_path
    passphrase   = args.passphrase

    # generate keys
    generate_keys(secrets_path, passphrase)
