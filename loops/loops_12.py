# Дана целочисленная матрица А[n,m]. Посчитать количество элементов матрицы,
# превосходящих среднее арифметическое значение элементов матрицы и сумма индексов которых четна.

# for i, number in enumerate(range(10, 15)):
#     print(f'i= {i}, n = {number}')
from random import randint

n = int(input("enter size n - "))
m = int(input("enter size m - "))

arr = [[randint(1, 9) for _ in range(m)] for _ in range(n)]
print(arr)

result_summ = 0
count = 0

for arr_i in arr:
    for i in arr_i:
        result_summ += i
        count += 1

result_avg = result_summ / count
print(f"average - {result_avg}")
count_01 = 0
for i, arr_i in enumerate(arr):
    for r, number in enumerate(arr_i):
        if number > result_avg and ((i * r) % 2) == 0:
            count_01 += 1
print(count_01)
