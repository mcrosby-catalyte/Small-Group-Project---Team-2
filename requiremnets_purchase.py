import data_table_purchases as data


def filter_purchaces(key, target_value):
    filtered = []
    for purchase in data.purchases:
        if getattr(purchase, key) == target_value:
            filtered.append(purchase)
    return filtered


def sort_purchaces(key, do_highest_to_lowest):
    if do_highest_to_lowest == True:
        pass
    else:
        pass
