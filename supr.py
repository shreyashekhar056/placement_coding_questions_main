#the super keyword in python is used in inheritance to refer to the parent class (also called the superclass).it allows you to access methods and properties from the parent class without directly naming it,especially useful for 
class Vehicle:
    def __init__(self, brand, fuel_type):
        self.brand = brand
        self.fuel_type = fuel_type
    def display_info(self):
        print(f"Brand  : {self.brand}")
        print(f"FuelType: {self.fuel_type}")
class Car(Vehicle):
    def __init__(self, brand, fuel_type, model):
        super().__init__(brand, fuel_type)  # Call the parent class constructor
        self.model = model

    def display_info(self):
        super().display_info()  # Call the parent class method
        print(f"Model  : {self.model}")

c= Car("Toyota", "Petrol", "Corolla")
c.display_info()