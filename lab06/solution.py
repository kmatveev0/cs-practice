from typing import Dict, List

def count_items(values: List) -> Dict:
    counts = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return counts

def unique_sorted(values: List) -> List:
    return sorted(set(values))

def common(first: List, second: List) -> List:
    return sorted((set(first)) & set(second))

def only_in_first(first: List, second: List) -> List:
    return sorted(set(first) - set(second))
