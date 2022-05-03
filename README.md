# requests-walmart-auth

This project provides python `requests` support for the [Walmart Affiliate Marketplace (REST) API](https://walmart.io/docs/affiliate/) required Additional Headers.

## Overview

The Affiliate Marketplace API requires `Additional Headers` to be included in each HTTPS request, as described in the [Onboarding Guide](https://walmart.io/docs/affiliate/onboarding-guide).

This project provides `requests` support for these `Additional Headers` via the `auth` interface.

## Requirements

- Python 3.7+
- pycryptodome ~=3.14.1
- requests ~=2.27.1

## Install

`requests-walmart-auth` can be installed from pypi via pip:

```shell
pip install requests-walmart-auth
```

## Usage

### `WalmartAuth`

The `WalmartAuth` class implements the `requests.auth.AuthBase` interface for use with `requests`.

```python
import requests
from   walmart_auth import WalmartAuth

# get auth
auth = WalmartAuth(consumer_id, private_key, key_version, passphrase=None)

# make request with auth
response = requests.get('https://...', auth=auth)
```

### WalmartSession

The `WalmartSession` class implements a persistent `requests.Session` with `WalmartAuth`.

```python
from walmart_auth import WalmartSession

# get session with persistent auth
session = WalmartSession(consumer_id, private_key, key_version, passphrase=None)

# make request; auth is transparent
session.get('https://...')
```

## Command Line Tools

### `generate-walmart-auth-keys`

This command line tool generates new key files as required for `Additional Headers`. This may come in handy in operating systems such as Windows that do not include tools like `openssh` by default.

From the help menu:

```comment
usage: generate-walmart-auth-keys [-h] secrets_path [passphrase]

generate keys for use with requests-walmart-auth

positional arguments:
  secrets_path
  passphrase

options:
  -h, --help    show this help message and exit
```

Three files are generated:

- `$SECRETS_PATH/public_key.pem`
- `$SECRETS_PATH/private_key.pem`
- `$SECRETS_PATH/public_key.b64.txt`

The last file is generated as a convenience: `Walmart.io` requires you to copy-paste the `public_key` without the `PEM` header and footer.

### `walmart-session`

This command line tool creates a new `WalmartSession` and provides a python REPL for experimentation.

From the help menu:

```comment
usage: walmart-session [-h] [--passphrase [PASSPHRASE]]
                       consumer_id private_key key_version

Start Walmart requests session

positional arguments:
  consumer_id
  private_key
  key_version

options:
  -h, --help            show this help message and exit
  --passphrase [PASSPHRASE], -p [PASSPHRASE]
```
