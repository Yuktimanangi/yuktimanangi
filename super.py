class vehicle:
    def __init__(self, brand, fuel_type):
        self.brand = brand
        self.fuel_type = fuel_type

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Fuel Type: {self.fuel_type}")

class Car(vehicle):
    def __init__(self, brand, fuel_type, model):
        super().__init__(brand, fuel_type)  # Call parent constructor
        self.model = model

    def display_details(self):
        self.display_info()
        print(f"Model: {self.model}")

# Example usage
c1 = Car("Toyota", "Petrol", "Corolla")
c1.display_details()
