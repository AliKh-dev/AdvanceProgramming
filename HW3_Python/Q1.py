# This function find key of maximum and minimum value which in the dict
def key_max_and_min_value(entry: dict) -> str:
    maximum = max(entry.values())
    minimum = min(entry.values())
    key_maximum = None
    key_minimum = None
    for key in entry.keys():
        if entry[key] == maximum:
            key_maximum = key
        if entry[key] == minimum:
            key_minimum = key
    return key_maximum, key_minimum


# print(key_max_and_min_value({'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}))
