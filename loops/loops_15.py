# Написать игру. Пользователь должен угадать число. Сперва вводится диапазон угадывания.
# После колличество попыток. В случае правильного ответа - выводить You are the winner.
# В случае неправильного давать игроку подсказку(больше или меньше искомое число).
# Если за указанное количество попыток число не угадано - выводить: You are the loser и правильное число.
from random import randint

number_range_from = int(input("from - "))
number_range_before = int(input("to - "))
number_attempts = int(input("number of attempts - "))
random_number = randint(number_range_from, number_range_before)
your_number = None

while number_attempts != 0:
    your_number = int(input("your number - "))
    if your_number == random_number:
        print("You are the winner")
        break
    if your_number < random_number:
        print("need more")
        number_attempts = number_attempts - 1
        print("attempts left -", number_attempts)
    if your_number > random_number:
        print("need less")
        number_attempts = number_attempts - 1
        print("attempts left -", number_attempts)
    if number_attempts == 0:
        print("You are the loser", random_number)
