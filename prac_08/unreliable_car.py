from prac_08.car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        start = random.randint(0,100)
        if start < self.reliability:
            Car.drive(self, distance)
        else:
            print("Car didn't start")