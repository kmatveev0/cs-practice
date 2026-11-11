import numpy as np


print("Задание 1")

hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)

print("line:", line)
print("zeros:", zeros)
print("unknown_table:\n", unknown_table)
print("identity:\n", identity)


print("\nЗадание 2")

print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы c индексами 2-5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("В обратном порядке:", hours[::-1])


print("\nЗадание 3")

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18]
])

print("shape:", temperatures.shape)
print("ndim:", temperatures.ndim)
print("size:", temperatures.size)
print("Вторая строка, третий столбец:", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:")
print(temperatures[:2, 1:])
print("Центральный фрагмент 2x2:")
print(temperatures[0:2, 1:3])


print("\nЗадание 4")

matrix = np.arange(1, 26).reshape(5, 5)

first_rows = matrix[:3, :]
last_rows = matrix[-2:, :]
first_columns = matrix[:, :2]
middle = matrix[1:4, 2:5]
bottom_right = matrix[-2:, -2:]

print("Исходная матрица:")
print(matrix)

print("\nПервые три строки:")
print(first_rows)
print("shape:", first_rows.shape)

print("\nПоследние две строки:")
print(last_rows)
print("shape:", last_rows.shape)

print("\nПервые два столбца:")
print(first_columns)
print("shape:", first_columns.shape)

print("\nФрагмент строк 1–3 и столбцов 2–4:")
print(middle)
print("shape:", middle.shape)

print("\nПравый нижний блок 2x2:")
print(bottom_right)
print("shape:", bottom_right.shape)


print("\nЗадание 5")

vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
print("Изменённый vector:", vector)

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9
print("Изменённая small_matrix:")
print(small_matrix)

changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1

print("changed_hours:", changed_hours)
print("Исходный hours:", hours)

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100

print("Изменённая матрица:")
print(changed_matrix)

print("Исходная матрица:")
print(matrix)


print("\nЗадание 6")

numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print("numbers:", numbers)
print("table:")
print(table)
print("transposed:")
print(transposed)

print("Форма numbers:", numbers.shape)
print("Форма table:", table.shape)
print("Форма transposed:", transposed.shape)