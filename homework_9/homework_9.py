import dataclasses
import time


@dataclasses.dataclass
class Auto:
    brand: str
    age: int
    mark: str
    color: str = "black"
    weight: int = 2

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1
        print(f"auto.birthday= {self.age}")


@dataclasses.dataclass
class Truck(Auto):
    max_load: int = 200

    def move(self):
        print("attention")
        super().move()

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)

    @property
    def info(self):
        return f"{self.brand=} {self.age=} {self.mark=} {self.color=} {self.weight=} {self.max_load=}"


truck = Truck("Ford", 6, "Fusion", "black", 2, 100)
truck_two = Truck("Peugeot", 4, "806", "silver", 2, 120)


@dataclasses.dataclass
class Car(Auto):
    max_speed: int = 0

    @classmethod
    def from_auto(cls, auto: Auto, max_speed: int):
        return cls(
            brand=auto.brand,
            age=auto.age,
            mark=auto.mark,
            color=auto.color,
            weight=auto.weight,
            max_speed=max_speed,
        )

    def move(self):
        super().move()
        print(f"max_speed is {self.max_speed}")

    @property
    def info(self):
        return f"{self.brand=} {self.age=} {self.mark=} {self.color=} {self.weight=} {self.max_speed=}"


auto = Auto("Ford", 6, "Fusion", "green", 8)
print(Car.from_auto(auto=auto, max_speed=340))
