class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of Doors: {self.num_doors}")


class Truck(Vehicle):
    def __init__(self, make, model, year, cargo_capacity):
        super().__init__(make, model, year)
        self.cargo_capacity = cargo_capacity

    def display_info(self):
        super().display_info()
        print(f"Cargo Capacity: {self.cargo_capacity} tons")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, drive_type):
        super().__init__(make, model, year)
        self.drive_type = drive_type

    def display_info(self):
        super().display_info()
        print(f"Drive Type: {self.drive_type}")


# Example Usage:
car = Car("Toyota", "Corolla", 2020, 4)
truck = Truck("Ford", "F150", 2019, 2.5)
motorcycle = Motorcycle("Honda", "CBR600", 2021, "Chain")

car.display_info()
truck.display_info()
motorcycle.display_info()
