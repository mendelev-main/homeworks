def read():
    number_one = read_number()
    my_sign = input("enter sign - ")
    number_two = read_number()
    if my_sign == "+":
        print(number_one + number_two)


def read_number():
    while True:
        try:
            return int(input("enter number - "))
        except ValueError:
            print('You entered bed data')


while True:
    read()
