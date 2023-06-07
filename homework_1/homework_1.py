# 1. Написать функцию read_humans, которая принимает аргументом название
# csv-файла, и возвращает список
# словарей (персонажей), у которых species это human
# 2. Написать функцию to_json, которая принимает аргументом список словарей и
# название json-файла, и записывает
# в файл список словарей в формате json (с индентацией в 4 пробела)
# 3. Вызвать функцию read_humans, ее результат передать в функцию to_json
import csv
import json


def read_humans(csv_file):
    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)
        sort_species = []
        for card_person in reader:
            if card_person["Species"] == "Human":
                sort_species.append(card_person)
        return sort_species


print(read_humans("characters.csv"))


def to_json(dictionary_list, file_name_json):
    with open(file_name_json, "w") as file:
        json.dump(dictionary_list, file, indent=4)


to_json(read_humans("characters.csv"), "people.json")
