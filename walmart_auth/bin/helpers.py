import code
import os
from   pathlib import Path
import sys


def interact_with_code(local):
    # include current directory
    # in python import paths
    current_dir = os.getcwd()
    sys.path.insert(0, current_dir)

    # interact
    message = ''
    code.interact(message, local=local)


def is_file(file):
    file = Path(file)
    if not file.exists():
        return False
    return file.is_file()


def read_key_file(file):
    assert is_file(file)
    file = Path(file)
    with file.open() as f:
        return f.read()
