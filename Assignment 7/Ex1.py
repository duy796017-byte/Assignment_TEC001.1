import random
class Car:
    def __init__(self, registration, max_speed):
        self.registration = registration
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0

    def accelerate(self, change):
        self.speed += change
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        elif self.speed < 0:
            self.speed = 0
    def drive(self, hours):
        self.distance += self.speed * hours
car_test = Car("ABC-123", 142)
car_test.accelerate(30)
print(f"Speed after +30 km/h: {car_test.speed}")
car_test.accelerate(70)
print(f"Speed after +70 km/h: {car_test.speed}")
car_test.accelerate(50)
print(f"Speed after +50 km/h: {car_test.speed}")
car_test.accelerate(-200)
print(f"Speed after emergency brake: {car_test.speed}")
print("\n--- Start racing ---\n")
cars = []
for i in range(1, 11):
    reg = "ABC-" + str(i)
    max_s = random.randint(150, 200)
    cars.append(Car(reg, max_s))
finished = False
hour = 0
while not finished:
    hour += 1
    for car in cars:
        change = random.randint(-10, 15)
        car.accelerate(change)
        car.drive(1)
        if car.distance >= 10000:
            finished = True
print("Final result:")
print(f"{'Plate':8} | {'Max':4} | {'Speed':6} | {'Distance':8}")
print("-" * 45)

for car in cars:
    print(
        f"{car.registration:8} | "
        f"{car.max_speed:4} | "
        f"{car.speed:6} | "
        f"{int(car.distance):8}"
    )