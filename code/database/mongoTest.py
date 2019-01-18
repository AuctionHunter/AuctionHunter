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
        self.db = self.client.admin
        self.posts = self.db.posts

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
        result = self.posts.insert_one(post_data)
        return result 

    def getVehicle(self, vin):
        retrieve_post = self.posts.find_one({"vin": vin})
        return retrieve_post

def main():
    database = Database("localhost", 27017)
    database.establishConnection()

    condition1 = Condition("Collision", "Right Side", "None", "Runs", "Present", "Standard Wheels and spare present", "Deployed")
    vehicle1 = Vehicle(1234512345, "Ford", "Focus", "SE", 2012, "Hatchback", "Standard", "Red", 34242, condition1)

    result = database.addVehicle(vehicle1)
    print(result)
    print('One post: {0}'.format(result.inserted_id))

    result = database.getVehicle("1234512345")
    print(result)
    print('One post: {0}'.format(result.inserted_id))

def main2():

    #Establish connection
    client = MongoClient("localhost", 27017)
    #Access Database
    db = client.admin
    #post data
    posts = db.posts
    post_data = {
        'make': 'Ford',
        'model': 'Focus',
        'year': '2012',
        'color': 'Red',
        'damage': 'lots'
    }
    result = posts.insert_one(post_data)
    print(result)
    print('One post: {0}'.format(result.inserted_id))

    post_1 = {
        'make': 'Honda',
        'model': 'Civic',
        'year': '2014',
        'color': 'Black',
        'damage': 'none'
    }
    post_2 = {
        'make': 'Toyota',
        'model': 'Corolla',
        'year': '2013',
        'color': 'Blue',
        'damage': 'minimal'
    }
    result = posts.insert_many([post_1, post_2])
    print('Multiple posts: {0}'.format(result.inserted_ids))

    #Retrieve data
    retrive_post = posts.find_one({"author": "Honda"})
    print(retrive_post)

if __name__ == "__main__":
    main()