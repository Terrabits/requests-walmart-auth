from .helpers     import interact_with_code
from argparse     import ArgumentParser
from walmart_auth import WalmartSession


def main():
    # command line interface (CLI)
    parser = ArgumentParser(description='Start Walmart requests session')
    parser.add_argument('--passphrase', '-p', nargs='?', default=None)
    parser.add_argument('consumer_id')
    parser.add_argument('private_key')
    parser.add_argument('key_version')


    # parse
    args         = parser.parse_args()
    consumer_id  = args.consumer_id
    private_key  = args.private_key
    passphrase   = args.passphrase
    key_version  = args.key_version

    if is_file(private_key):
        private_key = read_key_file(private_key)

    # open session
    session = WalmartSession(consumer_id, private_key, key_version, passphrase)

    # provide user REPL to
    # interact with session
    locals  = {
        'consumer_id': consumer_id,
        'private_key': private_key,
        'passphrase':  passphrase,
        'key_version': key_version,
        'session':     session,
    }
    interact_with_code(locals)
