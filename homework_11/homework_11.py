# Пройтись по собственноручно-написанной функции-генератору fibonacci, которая йилдит первые n чисел Фибоначчи:
# for i in fibonacci(10):
#     print(i)
# Вывод:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34

def fibonacci(n):
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b


for i in fibonacci(10):
    print(i)
