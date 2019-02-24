from mongoTest import Condition
from mongoTest import Vehicle
from mongoTest import Database

def main():
    database = Database("localhost", 27017)
    database.establishConnection()

    condition1 = Condition("Collision", "Right Side", "None", "Runs", "Present", "Standard Wheels and spare present", "Deployed")
    vehicle1 = Vehicle(1234512345, "Ford", "Focus", "SE", 2012, "Hatchback", "Standard", "Red", 34242, condition1)
    result = database.addVehicle(vehicle1)
    print(result)

if __name__ == "__main__":
    main()