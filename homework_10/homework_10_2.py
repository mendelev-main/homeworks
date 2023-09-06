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


with open("cars.json", "r", encoding="utf-8") as f:
    text = json.load(f)

my_cars = []
for i in text:
    try:
        car = Car(
            make=i["make"],
            model=i["model"],
            year=i["year"],
            price=i["price"],
            color=i["color"],
            mileage=i["mileage"],
        )
    except KeyError:
        continue
    my_cars.append(car)

ford_mustang = [
    car.price for car in my_cars if car.make == "Ford" and car.model == "Mustang"
]

print(f"average cost Ford Mustang - {int(sum(ford_mustang) / len(ford_mustang))}")
