# Получить сумму кубов натуральных чисел от n до m, используя цикл for

n = int(input("От "))
m = int(input("До ")) + 1
n_m = range(n, m)
count = 0
for i in n_m:
    count += i**3
print(count)
