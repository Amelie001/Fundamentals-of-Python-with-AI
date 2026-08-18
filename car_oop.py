class Car:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def accelerate(self):
        self.speed += 10

car = Car("Toyota", 50)

car.accelerate()
car.accelerate()

print("Brand:", car.brand)
print("Speed:", car.speed)