# Задание #34
# Используя библиотеки threading и requests собрать данные об университетах любых 10 стран (вот api), и записать
# в соответствующий country_name.json файл (форматируя по 2 отступа).
# По одному потоку на страну. Эту домашку нужно делать в репе с остальными домашками (не с ботом или джангой)

import json
import threading

from requests import request

countries = [
    "Germany",
    "Poland",
    "Bulgaria",
    "Austria",
    "Belgium",
    "Belarus",
    "Norway",
    "Sweden",
    "Denmark",
    "Spain",
]


def get_university_data(country):
    print(country)
    response = request(
        "GET", f"http://universities.hipolabs.com/search?country={country}"
    )

    json_data = response.json()
    print(json.dumps(json_data, indent=2))

    with open(f"{country}.json", "w") as file:
        json.dump(json_data, file, indent=2)


threads = []

for country in countries:
    thread = threading.Thread(target=get_university_data, args=(country,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("end")
