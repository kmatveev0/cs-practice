def count_items(values: List) -> Dict:
    counts = {}
    for value in values:
        count_items(values) = counts.get(values, 0) + 1
    return count_items

def unique_sorted(values: List) -> List:
    return sorted(set(valuues))

def common(first: List, second: List) -> List:
    return sorted(set(first)) & set(second))

def only_in_first(first: List, second: List) -> List:
    return sorted(set(first) - set(second))
