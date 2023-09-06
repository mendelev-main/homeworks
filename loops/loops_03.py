# Просуммировать неопределенное количество чисел, вводимых пользователем, суммировать до тех пор,
# пока пользователь не введёт слово «стоп»

count = 0
while True:
    number = input("num - ")
    if number != "стоп":
        count = count + int(number)
        print(count)
    else:
        break
