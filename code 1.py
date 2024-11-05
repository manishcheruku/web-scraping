class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"Car Make: {self.make}, Model: {self.model}"

my_car = Car("Toyota", "Camry")
my_car1 = Car("Volvo", "x6")
print((my_car1.display_info(),my_car.display_info()))
