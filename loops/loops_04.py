# Просуммировать неопределенное количество чисел, вводимых пользователем, суммировать до тех пор,
# пока пользователь не введёт слово «стоп». Не учитывать числа кратные 5

count = 0
while True:
    number = input("num - ")
    if number == "стоп":
        break
    if int(number) % 5 == 0:
        print(count)
        continue
    else:
        count = count + int(number)
        print(count)
