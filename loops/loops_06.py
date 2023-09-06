# Написать программу, которая будет выводить на экран случайные числа от 1 до 10 до тех пор,
# пока не выпадет 7.

from random import randint

while True:
    my_random = randint(1, 10)
    print(my_random)
    if my_random == 7:
        break
