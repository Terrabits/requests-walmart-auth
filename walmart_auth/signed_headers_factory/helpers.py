def to_bytes(headers):
    """convert headers to canonical bytes array for signing"""
    values = values_sorted_by_key(headers)
    values_str = '\n'.join(values) + '\n'
    return values_str.encode()


# helpers helpers


def values_sorted_by_key(_dict):
    """returns list of values of _dict sorted by key"""
    return [_dict[key] for key in sorted(_dict.keys())]
