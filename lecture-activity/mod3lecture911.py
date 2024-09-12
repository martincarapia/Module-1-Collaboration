"""
Write a Python app that has the following classes:
A super class called Vehicle, which contains an attribute for vehicle type, such as car, truck, plane, boat, or a broomstick.
A class called Automobile which will inherit the attributes from Vehicle and also contain the following attributes:
year
make
model
doors (2 or 4)
roof (solid or sun roof).
Write an app that will accept user input for a car. The app will store "car" into the vehicle type in your Vehicle super class. 
The app will then ask the user for the year, make, model, doors, and type of roof and store the data in the attributes above.
The app will then output the data in an easy-to-read and understandable format, such as this:
  Vehicle type: car
  Year: 2022
  Make: Toyota
  Model: Corolla
  Number of doors: 4
  Type of roof: sun roof
"""
class Vehicle:
    def __init__(self, vehicle_type: str) -> None:
        self.vehicle_type = vehicle_type
        pass
    
class Automobile(Vehicle):
    def __init__(self, vehicle_type: str, year: int, make: str, model: str, num_of_doors: int, roof_type: str) -> None:
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.num_of_doors = num_of_doors
        self.roof_type = roof_type
    
    def output_automobile(self):
        return(f"Vehicle Type: {self.vehicle_type}\nYear: {self.year}\nMake:{self.make}\nModel: {self.model}\nNumber of doors: {self.num_of_doors}\nRoof Type: {self.roof_type}")


while True:
    print("Hello, thank you for trying the Car builder!")

    year = input("What's the year of the car: ")
    make = input("What's the make of the car: ")
    model = input("What's the model of the car: ")
    amt_of_doors = input("How many doors does it have: ")
    type_of_roof = input("What kind of roof do you have? [Regular or Sun] ")

    user_vehicle = Automobile("Car", year, make, model, amt_of_doors, type_of_roof)

    print("Here is the Car's information!\n", user_vehicle.output_automobile())


