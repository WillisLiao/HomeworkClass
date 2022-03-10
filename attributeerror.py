class Car:
    def __init__(self, model, max_speed):
        self.model = model
        self.max_speed = max_speed
car1 = Car("Tesla", "200km/hr")
print("car1's max_speed is{}".format(car1.max_speed))
print("car1's price is{}".format(car1.price))