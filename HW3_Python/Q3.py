def lists_to_dict(keys: list, values: list) -> dict:
    # if len(keys) != len(values):
    #     return "The numbers of values are'nt equal to numbers of keys!"
    for key in keys:
        if isinstance(key, set) or isinstance(key, dict):
            return "One or more key in your keys are'nt hashable"
    dictionary = dict()
    minimum_range = min(len(keys), len(values))
    for i in range(minimum_range):
        dictionary[keys[i]] = values[i]
    return dictionary


# print(lists_to_dict(['a', 'b', 'c', 'd', 'e', 'f'],[1, 2, 3, 4, 5]))
