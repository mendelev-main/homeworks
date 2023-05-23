import time


class Auto:

    def __init__(self, brand, age, mark, color='black', weight=2):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1
        print(f'auto.birthday= {self.age}')


auto = Auto('Ford', 6, 'Fusion', 'green', 8)


class Truck(Auto):
    def __init__(self, brand, age, mark, color, weight, max_load):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print("attention")
        super().move()

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)


truck = Truck('Ford', 6, 'Fusion', 'black', 2, 100)
truck_two = Truck('Peugeot', 4, '806', 'silver', 2, 120)

print('/////////////////////////////////truck/////////////////////////////////')
print(f'{truck.brand=}\n{truck.age=}\n{truck.mark=}\n{truck.color=}\n{truck.weight=}\n{truck.max_load=}')
truck.move()
truck.load()

print('///////////////////////////////truck_two///////////////////////////////')
print(f'{truck_two.brand=}\n{truck_two.age=}\n{truck_two.mark=}\n{truck_two.color=}\n'
      f'{truck_two.weight=}\n{truck_two.max_load=}')
truck_two.move()
truck_two.load()


class Car(Auto):
    def __init__(self, brand, age, mark, color, weight, max_speed):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'max_speed is {self.max_speed}')


car = Car('Ford', 6, 'Fusion', 'black', 2, 320)
car_two = Car('Peugeot', 4, '806', 'silver', 2, 210)

print('//////////////////////////////////car//////////////////////////////////')
print(f'{car.brand=}\n{car.age=}\n{car.mark=}\n{car.color=}\n{car.weight=}\n{car.max_speed=}')
car.move()

print('////////////////////////////////car_two////////////////////////////////')
print(f'{car_two.brand=}\n{car_two.age=}\n{car_two.mark=}\n{car_two.color=}\n{car_two.weight=}\n{car_two.max_speed=}')
car_two.move()
