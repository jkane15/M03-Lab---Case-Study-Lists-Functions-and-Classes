class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        print("Vehicle type:", self.vehicle_type)
        print("Year:", self.year)
        print("Make:", self.make)
        print("Model:", self.model)
        print("Number of doors:", self.doors)
        print("Type of roof:", self.roof)


if __name__ == "__main__":
    
    vehicle_type = "car"  
    year = int(input("Enter the year of the car: "))
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    doors = int(input("Enter the number of doors (2 or 4): "))
    roof = input("Enter the type of roof (solid or sun roof): ")

    
    car1 = Automobile(vehicle_type, year, make, model, doors, roof)

    
    car1.display_info()

