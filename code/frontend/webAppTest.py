from mongoTest import Database

def getVehicleByVINTest(database):
    #Find vehicle with particular vin.
    result = database.getVehicle("1234512345")
    #Print the whole thing
    print(result)
    #Print certain attributes
    database.printEntry(result)

def getVehicleByYearTest(database):
    #get vehicles with year greater than 1999
    result_cursor = database.getVehiclesGTYear(1999)
    #iterate over the data retrieved and print
    count = result_cursor.collection.count_documents({})
    for x in range(count):
        current_entry = result_cursor.next()
        database.printEntry(current_entry, True)

def getAllVehiclesTest(database):
    #get all vehicle entries
    result_cursor = database.getAllVehicles()
    #iterate over the data retrieved and print
    count = result_cursor.collection.count_documents({})
    for x in range(count):
        current_entry = result_cursor.next()
        database.printEntry(current_entry)

def main():
    database = Database("localhost", 27017)
    database.establishConnection()

    #getAllVehiclesTest(database)
    getVehicleByYearTest(database)

    

if __name__ == "__main__":
    main()  