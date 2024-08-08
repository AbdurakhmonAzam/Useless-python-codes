def merge_dictionaries(dict1, dict2):
    merged_dict=dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

dict1={'Germany': 'Berlin', 'China': 'Beijing'}
dict2={'Korea': 'Seoul', 'France': 'Paris'}
print(merge_dictionaries(dict1, dict2))
