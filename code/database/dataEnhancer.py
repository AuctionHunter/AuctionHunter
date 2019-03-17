from pymongo import MongoClient
from sshtunnel import SSHTunnelForwarder
import time
import sys


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
    #database = Database("localhost", 27017)
    #database.establishConnection()

    MONGO_HOST = "theorange.institute"
    MONGO_DB = "scrapy"
    MONGO_USER = "hullale"
    MONGO_PASS = "unhackable"

    server = SSHTunnelForwarder(
    MONGO_HOST,
    ssh_username=MONGO_USER,
    ssh_port=22,
    ssh_password=MONGO_PASS,    
    remote_bind_address=('localhost', 27017)
    )

    server.start()
    time.sleep(2)

    print(server.local_bind_port)

    client = MongoClient('localhost', server.local_bind_port)
    
    #db = client[MONGO_DB]
    db = client.admin
    posts = db.posts

    result_cursor = posts.find()
    #result_cursor = database.getAllVehicles()
    #iterate over the data retrieved and print
    count = result_cursor.collection.count_documents({})
    print(count)
    for x in range(count):
        current_entry = result_cursor.next()
        #database.printEntry(current_entry)
        print("vin:" + str(current_entry.get("vin")) + " " + current_entry.get("exteriorColor") + " " + current_entry.get("make") + " " + 
        current_entry.get("model") + " " + str(current_entry.get("year")))

    server.stop()



if __name__ == "__main__":
    main()
