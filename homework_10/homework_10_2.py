# *2. Написать программу, которая считывает машины из cars.json и десериализует их в объекты датакласса Car.
# Нужно найти среднюю стоимость фордов мустангов. Обратите внимание, что некоторые записи не содержат информации о цене,
# такие записи нужно пропускать.
import dataclasses
import json


@dataclasses.dataclass
class Car:
    make: str
    model: str
    year: int
    price: int
    color: str
    mileage: int


with open('cars.json', 'r', encoding='utf-8') as f:
    text = json.load(f)

my_cars = []
for i in text:
    try:
        car = Car(i['make'], i['model'], i['year'], i['price'], i['color'], i['mileage'])
    except KeyError:
        continue
    if i['make'] == 'Ford' and i['model'] == 'Mustang':
        my_cars.append(car)

counter = 0
for car in my_cars:
    counter += car.price
print(f'average cost Ford Mustang - {int(counter / len(my_cars))}')
