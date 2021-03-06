import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "my-test-db"
COLLECTION_NAME = "myFirstMDB"

def mongo_connection(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connectto MongoDB: %s") % e

conn = mongo_connection(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

coll.update_many({'nationality': 'american'}, {'$set': {'hair_colour': 'maroon'}})

documents = coll.find({'nationality': 'american'})

for doc in documents:
    print(doc)