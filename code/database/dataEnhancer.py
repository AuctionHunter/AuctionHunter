from pymongo import MongoClient

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

    def printEntry(self, entry, verbose=False):
        if(verbose):
            print("vin:" + str(entry.get("vin")) + " " + entry.get("exteriorColor") + " " + entry.get("make") + " " + entry.get("model")
            + " " + str(entry.get("year")))
        else:
            print(entry.get("make") + " " + entry.get("model")
            + " " + str(entry.get("year")))

    def getAllVehicles(self):
        retrieve_cursor = self.posts.find()
        return retrieve_cursor

def main():
    database = Database("localhost", 27017)
    database.establishConnection()

    #result_cursor = database.getAllVehicles()
    #iterate over the data retrieved and print
    count = result_cursor.collection.count_documents({})
    print(count)
    for x in range(count):
        current_entry = result_cursor.next()
        #database.printEntry(current_entry)
        print("vin:" + str(current_entry.get("vin")) + " " + current_entry.get("exteriorColor") + " " + current_entry.get("make") + " " + 
        current_entry.get("model") + " " + str(current_entry.get("year")))



if __name__ == "__main__":
    main()
