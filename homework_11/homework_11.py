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
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


for i in fibonacci(10):
    print(i)
