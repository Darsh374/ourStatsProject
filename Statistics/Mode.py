import collections
def mode(data):
    countItems = collections.Counter(data)
    data_list = dict(countItems)
    max_value = max(list(countItems.values()))
    mode_val = [num for num, freq in data_list.items() if freq == max_value]
    if len(mode_val) == len(data):
        return("No mode in the list")
    else:
        return mode_val


