# Ввести два целых числа a и b ( a < b ). Вывести в порядке возрастания все целые числа,
# расположенные между a и b (включая сами числа a и b ), а также количество n этих чисел.

a = int(input("Число a "))
b = int(input("Число b ")) + 1
a_b = list(range(a, b))
n = 0
while n < len(a_b):
    n += 1
print(f"n = {n}  a,b = {a_b}")
