




from abc import ABC, abstractmethod




class DriveStrategy(ABC):

    @abstractmethod
    def drive(self):
        pass


class Vehicle:

    def __init__(self, drive_strategy: DriveStrategy):
        self.drive_strategy = drive_strategy

    def drive(self):
        # print(self.drive_strategy.drive())
        return self.drive_strategy.drive()




class NormalDrive(DriveStrategy):

    def drive(self):
        # print("Normal drive capability")
        return "Normal drive capability"



class SportsDrive(DriveStrategy):

    def drive(self):
        # print("Sports drive capability")
        return "Sports drive capability"




class PassengerDrive(DriveStrategy):

    def drive(self):
        # print("Passenger drive capability")
        return "Passenger drive capability"









# vehicle = Vehicle(NormalDrive())
# print(vehicle.drive())


# vehicle = Vehicle(SportsDrive())
# print(vehicle.drive())


class SportsVehicle(Vehicle):

    def __init__(self):
        super().__init__(Vehicle(SportsDrive()))



sv = SportsVehicle()

print(sv.drive())
