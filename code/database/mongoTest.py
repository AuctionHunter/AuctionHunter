from pymongo import MongoClient

class Condition:
    def __init__(self, typeDamage, primaryDamageLocation, secondaryDamageLocation, startCode, keyFOB, wheels, airbags):
        self.typeDamage = typeDamage
        self.primaryDamageLocation = primaryDamageLocation
        self.secondaryDamageLocation = secondaryDamageLocation
        self.startCode = startCode
        self.keyFOB = keyFOB
        self.wheels = wheels
        self.airbags = airbags

class Vehicle:
    def __init__(self, vin, make, model, series, year, bodyStyle, transmission, exteriorColor, odometer, condition):
        self.vin = vin
        self.make = make
        self.model = model
        self.series = series
        self.year = year
        self.bodyStyle = bodyStyle
        self.transmission = transmission
        self.exteriorColor = exteriorColor
        self.odometer = odometer
        self.condition = condition #condition object

class Database:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = MongoClient(host, port)
    
    def establishConnection(self):
        self.client = MongoClient(self.host, self.port)
        self.db = self.client.scrapy
        self.scrapy_items = self.db.scrapy_items

    def addVehicle(self, vehicle):
        post_data = {
            'vin': vehicle.vin,
            'make': vehicle.make,
            'model': vehicle.model,
            'series': vehicle.series,
            'year': vehicle.year,
            'bodyStyle': vehicle.bodyStyle,
            'transmission': vehicle.transmission,
            'exteriorColor': vehicle.exteriorColor,
            'odometer': vehicle.odometer,
            'typeDamage': vehicle.condition.typeDamage,
            'primaryDamageLocation': vehicle.condition.primaryDamageLocation,
            'secondaryDamageLocation': vehicle.condition.secondaryDamageLocation,
            'startCode': vehicle.condition.startCode,
            'keyFOB': vehicle.condition.keyFOB,
            'wheels': vehicle.condition.wheels,
            'airbags': vehicle.condition.airbags
        }
        result = self.scrapy_items.insert_one(post_data)
        return result 

    def printEntryDeprecated(self, entry, verbose=False):
        if(verbose):
            print("vin:" + str(entry.get("vin")) + " " + entry.get("exteriorColor") + " " + entry.get("make") + " " + entry.get("model")
            + " " + str(entry.get("year")))
        else:
            print(entry.get("make") + " " + entry.get("model")
            + " " + str(entry.get("year")))
    
    def printEntry(self, entry, verbose=False):
        if(verbose):
            print(str(entry.get("vin")) + " " + str(entry.get("miles")) + " " + str(entry.get("car name")) + " " + str(entry.get("primary damage")))
        else:
            print(str(entry.get("car name")))

    def getVehicleByVin(self, vin):
        retrieve_post = self.scrapy_items.find_one({"vin": int(vin)})
        return retrieve_post

    def getAllVehicles(self):
        retrieve_cursor = self.scrapy_items.find()
        return retrieve_cursor

    def getVehiclesGTYear(self, year):
        retrieve_cursor = self.scrapy_items.find({"year": {"$gt": int(year)}})
        return retrieve_cursor

def main():
    database = Database("localhost", 27017)
    database.establishConnection()

    #Create a condition object
    condition1 = Condition("Collision", "Right Side", "None", "Runs", "Present", "Standard Wheels and spare present", "Deployed")
    #Create a vehicle object with the condition1 attribute
    vehicle1 = Vehicle(1234512345, "Ford", "Focus", "SE", 2012, "Hatchback", "Standard", "Red", 34242, condition1)

    #Add the vehicle to the database
    result = database.addVehicle(vehicle1)
    print(result)
    #print('One post: {0}'.format(result.inserted_id))

    #Get a vehicle based on the VIN
    result = database.getVehicleByVin("1234512345")
    #Print the whole thing
    print(result)
    #Print certain attributes
    print(result.get("make") + " , " + result.get("model") + " ," + str(result.get("year")))

if __name__ == "__main__":
    main()
