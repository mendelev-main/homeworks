# Ввести с клавиатуры целое число n.
# Получить сумму кубов всех целых чисел от 1 до n(включая n) используя цикл while

numbers = int(input("enter number - "))
my_num = 1
my_sum = 0
while my_num <= numbers:
    my_sum += my_num**3
    my_num += 1
print(my_sum)

# or

my_num_1 = sum([(my_num**3) for my_num in range(1, numbers + 1)])
print(my_num_1)
