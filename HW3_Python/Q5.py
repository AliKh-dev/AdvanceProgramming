def combine_dicts(*dictionaries: dict) -> dict:
    new_dict = dict()
    for dictionary in dictionaries:
        for key, value in dictionary.items():
            if new_dict.get(key) == None:
                new_dict[key] = list()
                new_dict[key].append(value)
            else:
                new_dict[key].append(value)
    return new_dict


# print(combine_dicts({'w': 50, 'x': 100, 'y': 'Green', 'z': 400},
#                     {'x': 300, 'y': 'Red', 'z': 600}))
