def dict_to_list(dictionary: dict) -> list:
    list_of_tuple = list()
    for key, value in dictionary.items():
        list_of_tuple.append((key, value))
    return list_of_tuple

# print(dict_to_list({'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}))
