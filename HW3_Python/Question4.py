def find_all_keys(dictionary: dict, value: int or str) -> tuple:
    list_keys = list()
    for k, v in dictionary.items():
        if v == value:
            list_keys.append(k)
    return tuple(list_keys)


# print(find_all_keys(
#     {'Theodore': 19, 'Roxanne': 22, 'Mathew': 19, 'Betty': 20, }, 19))
