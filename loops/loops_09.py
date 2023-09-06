# Создать квадратную матрицу размерностью n и заполнить ее случайными значениями от 1 до 9.

from random import randint

n = int(input("Размер матрицы: "))

matrix = []
for i in range(n):
    column = []
    for j in range(n):
        column.append(randint(1, 9))
    matrix.append(column)
    print(*column)
