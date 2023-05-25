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

    @property
    def info(self):
        return f'{self.brand=} {self.age=} {self.mark=} {self.color=} {self.weight=} {self.max_load=}'


truck = Truck('Ford', 6, 'Fusion', 'black', 2, 100)
truck_two = Truck('Peugeot', 4, '806', 'silver', 2, 120)

print(truck.info)
truck.move()
truck.load()

print(truck_two.info)
truck_two.move()
truck_two.load()


class Car(Auto):
    def __init__(self, brand, age, mark, color, weight, max_speed):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'max_speed is {self.max_speed}')

    @property
    def info(self):
        return f'{self.brand=} {self.age=} {self.mark=} {self.color=} {self.weight=} {self.max_speed=}'


car = Car('Ford', 6, 'Fusion', 'black', 2, 320)
car_two = Car('Peugeot', 4, '806', 'silver', 2, 210)

print(car.info)
car.move()
print(car_two.info)
car_two.move()
