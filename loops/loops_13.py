# Создать список с фамилиями. Вывести все фамилии, которые начинаются на P(ANGL) и заканчиваются на а(ANGL)
lust_name = input("enter lust name - ").split(" ")
lust_name_list = list(lust_name)
print(lust_name_list)

for i in lust_name_list:
    if i[0] == "P" and i[-1] == "a":
        print(i)
