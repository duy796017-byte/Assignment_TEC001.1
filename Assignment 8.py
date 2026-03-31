import random

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom = bottom_floor
        self.top = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1

    def go_to_floor(self, target):
        while self.current_floor < target:
            self.floor_up()
        while self.current_floor > target:
            self.floor_down()

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom = bottom_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, index, destination):
        self.elevators[index].go_to_floor(destination)

    def fire_alarm(self):
        for e in self.elevators:
            e.go_to_floor(self.bottom)

class Car:
    def __init__(self, name):
        self.name = name
        self.speed = 0
        self.distance = 0

    def drive(self, hours):
        self.distance += self.speed * hours

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance   # ✅ FIX
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.speed = max(0, car.speed + change)
            car.drive(1)

    def print_status(self):
        for car in self.cars:
            print(f"{car.name} {car.speed} {car.distance}")

    def race_finished(self):
        return any(car.distance >= self.distance for car in self.cars)

if __name__ == "__main__":

    e = Elevator(1, 10)
    e.go_to_floor(5)
    e.go_to_floor(1)

    b = Building(1, 10, 3)
    b.run_elevator(0, 7)
    b.fire_alarm()

    cars = [Car(f"Car{i}") for i in range(1, 11)]
    race = Race("Grand Demolition Derby", 8000, cars)

    hours = 0
    while not race.race_finished():
        race.hour_passes()
        hours += 1

        if hours % 10 == 0:
            race.print_status()

    race.print_status()