# Дан двумерный массив n × m элементов. Определить, сколько раз встречается число 7 среди элементов массива.
from random import randint

n = int(input("enter size n - "))
m = int(input("enter size m - "))

matrix = []
number_7 = 0
for i in range(n):
    column = []
    for j in range(m):
        column.append(randint(1, 9))
    matrix.append(column)
    print(column)

for matrix_i in matrix:
    for i in matrix_i:
        if i == 7:
            number_7 += 1
print(number_7)
