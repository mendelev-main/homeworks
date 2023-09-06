# Создать квадратную матрицу размерностью n и заполнить ее случайными значениями.
# Нвйти сумму всех элементов
# Найти сумму всех элементов матрицы, которые кратны 3.

from random import randint

n = int(input("Размер матрицы: "))

matrix = []
for i in range(n):
    column = []
    for j in range(n):
        column.append(randint(1, 9))
    matrix.append(column)
    print(*column)

# result_sum = 0
# for matrix_1 in matrix:
#     print(matrix_1)
#     for i in matrix_1:
#         result_sum += i
# print(result_sum)
#
# result_sum = 0
# for matrix_1 in matrix:
#     print(matrix_1)
#     for i in matrix_1:
#         if i % 3 == 0:
#             result_sum += i
# print(result_sum)
