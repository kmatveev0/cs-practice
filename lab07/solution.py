from typing import Dict, List
import numpy as np

def reshape_rows(values: List[float], width: int) -> List[List[float]]:
    arr = np.asarray(values, dtype=float)
    if (arr.size != 0) and (arr.size % width == 0):
        return arr.reshape(arr.size // width, -1)
    else:
        return []

def block(matrix: List[List[float]], rows: List[int], collumns: List[int]) -> List[List[float]]:
    arr = np.asarray(matrix, dtype=float)
    if arr.size == 0:
        return []
    return (arr[np.ix_(rows, collumns)]).tolist()

def column_means(matrix: List[List[float]]) -> List[float]:
    if not matrix:
        return []
    arr = np.asarray(matrix, dtype=float)
    if arr.size == 0:
        return []
    return np.round(arr.mean(axis=0),6).tolist()

def column_range(matrix: List[List[float]], column: int) -> float:
    if not matrix:
        return []
    arr = np.asarray(matrix, dtype=float)
    if arr.size == 0:
        return []
    values = arr[:, column]
    return round(float(np.max(values) - np.min(values)), 6)

"""
values = [12.0, 14.5, 11.0, 13.0, 15.5, 10.5]
def1 = reshape_rows(values, 3)
print(def1)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def2 = block(matrix, [0, 2], [1, 2])
print(def2)

def3 = column_means(matrix)
print(def3)

def4 = column_range([[1, 2], [5, 7]], 1)
print(def4)
"""
