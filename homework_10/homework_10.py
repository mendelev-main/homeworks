# 1. Написать программу, которая загадывает число от 0 до 100 (см random.randint в документации).
# Пользователь вводит число, и программа выводит > или < или =. Потом пользователь снова вводит число и тд,
# до тех пор пока число не будет равно загаданному. Когда пользователь ввел число, которое равно загаданному,
# программа останавливается. При помощи try/except нужно пытаться считать ввод пользователя до тех пор, пока пользователь
# не введет число.

from random import randint


def comparison():
    random_number = randint(0, 100)

    while True:
        custom_number = [entered_number()]
        if int(*custom_number) < random_number:
            print('your number < hidden number')
        if int(*custom_number) > random_number:
            print('your number > hidden number')
        if int(*custom_number) == random_number:
            print('you guessed')
            break


def entered_number():
    while True:
        try:
            return int(input('Enter your number - '))
        except ValueError:
            print('You entered bed data')


comparison()
