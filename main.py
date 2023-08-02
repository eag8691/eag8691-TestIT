class Vehicle:
    """A class representing any type of vehicle"""

    def SetVehicleMake(self, make):
        """Input make of vehicle"""
        self.make = make

    def SetVehicleModel(self, model):
        """Input model of vehicle"""
        self.model = model

    def GetVehicleMake(self):
        """Print out make of vehicle"""
        print(f"\nThe make of the vehicle is a {self.make}.")

    def GetVehicleModel(self):
        """Print out model of vehicle"""
        print(f"The model of the vehicle is a {self.model}.")

class Car(Vehicle):
    """Represent aspects of a vehicle, specific to cars"""

    def SetCarDoor(self, doors):
        """Set number of doors a car has."""

        self.car_door = doors

    def GetCarDoor(self):
        """Print number of doors car has."""

        print(f"A {self.make} {self.model} has {self.car_door} doors.")

class Truck(Vehicle):
    """Represent aspects of a vehicle, specific to trucks."""

    def SetBedLength(self, length):
        """Set length of truck bed."""

        self.bed_length = length

    def GetBedLength(self):
        """Print length of truck bed."""

        print(f"A {self.make} {self.model} has a bed length of {self.bed_length}.")


print("Welcome to the Virtual Garage")

while True: 
  option = input("\nPlease press 1 to make a car, 2 to make a truck, or 3 to quit: ")


  if option == '1':
    input_make = input("Please enter your car make: ")
    input_model = input("Please enter your car model: ")
    input_drs = input("Please enter the number of doors: ")
    new_car = Car()
    new_car.SetVehicleMake(input_make)
    new_car.SetVehicleModel(input_model)
    new_car.SetCarDoor(input_drs)
    new_car.GetVehicleMake()
    new_car.GetVehicleModel()
    new_car.GetCarDoor()
    print("Your car has been added to the Garage.")

  elif option == '2':
    input_make = input("Please enter your truck make: ")
    input_model = input("Please enter your truck model: ")
    input_bed_length = input("Please enter the length of the truck bed: ")
    new_truck = Truck()
    new_truck.SetVehicleMake(input_make)
    new_truck.SetVehicleModel(input_model)
    new_truck.SetBedLength(input_bed_length)
    new_truck.GetVehicleMake()
    new_truck.GetVehicleModel()
    new_truck.GetBedLength()
    print("Your truck has been added to the garage.")

  else:
    print("Thank you for trying out the Virtual Garage!")
    break


      




        