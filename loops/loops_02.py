# Дан произвольный список, содержащий только числа. Выведите результат сложения всех чисел больше 10.

my_count = input("numbers - ").split(" ")
my_sum = 0
for number in my_count:
    if int(number) > 10:
        my_sum += int(number)
print(my_sum)
