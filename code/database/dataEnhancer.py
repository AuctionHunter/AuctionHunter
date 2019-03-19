from pymongo import MongoClient
from mongoTest import Database

class DataEnhancer:
    #milesWeight ~= 0-30
    #damageWeight ~= 0-10
    def __init__(self, milesWeight, damageWeight):
        self.milesWeight = milesWeight
        self.damageWeight = damageWeight

    #Return miles as an int in thousands of miles
    def parseMiles(self, milesString):
        sanitizedString = milesString.strip().split("k")[0]
        #Sometimes entry is 0-1, which we assume to be 0
        if("-" in sanitizedString):
            return 0
        else:
            return int(milesString.strip().split("k")[0])

    #return damage value of -5 to 0. 
    def parseDamage(self, damageString):
        damageValue = 0
        if("Collision" in damageString):
            damageValue += 1
        if("FRONT" in damageString):
            damageValue += 1
        if("REAR" in damageString):
            damageValue += 1
        if("SIZE" in damageString):
            damageValue += 1
        if("ENGINE" in damageString):
            damageValue += 3

        return damageValue

    def getValueEstimation(self, entry):
        milesString = str(entry.get("miles"))
        damageString = str(entry.get("primary damage"))
        
        miles = self.parseMiles(milesString)
        damage = self.parseDamage(damageString)

        #initial value of 50     
        value = 50
        #Add or subtract value based on miles and milesWeight. 
        #If miles=0k, add milesWeight value, if miles=150k subtract milesWeight. 
        #If miles=75k, don't change value. 
        value -= ((miles*2)/150.0 - 1)*self.milesWeight

        #Damage from 0 to 5(most impactful damage) 
        value -= damage*(self.damageWeight/2.0)
        
        return value


def main():
    database = Database("localhost", 27017)
    enhancer = DataEnhancer(20,10)

    database.establishConnection()

    result_cursor = database.getAllVehicles()
    #iterate over the data retrieved and print
    count = result_cursor.collection.count_documents({})
    for x in range(count):
        current_entry = result_cursor.next()
        database.printEntry(current_entry, False)
        #print(enhancer.parseMiles(str(current_entry.get("miles"))))
        #print(enhancer.parseDamage(str(current_entry.get("primary damage"))))
        value = enhancer.getValueEstimation(current_entry)
        currentVin = current_entry.get("vin")
        database.scrapy_items.update_one({"vin": currentVin}, {"$set": {"value_est": value}})

if __name__ == "__main__":
    main()
