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

new_docs =[{'first': 'terry', 'last': 'pratchett', 'dob': '28/04/1948', 
            'gender': 'm', 'hair_colour': 'not much', 'occupation': 'writer',
            'nationality': 'english'},
            {'first': 'george', 'last': 'rr martin', 'dob': '20/09/1948',
                'gender': 'm', 'hair_colour': 'white', 'occupation': 'writer',
                'nationality': 'american'}]


coll.insert_many(new_docs)

documents = coll.find()

for doc in documents:
    print(doc)