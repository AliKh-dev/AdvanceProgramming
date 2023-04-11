# This function find key of maximum and minimum value which in the dict
def key_max_and_min_value(values: dict) -> str:
    maximum = max(values.values())
    minimum = min(values.values())
    key_maximum = None
    for key in values.keys():
        if values[key] == maximum:
            key_maximum = key
        if values[key] == minimum:
            key_minimum = key
    return key_maximum, key_minimum


print(key_max_and_min_value({'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}))
