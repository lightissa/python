""" An example of how to insert a document """
import sys

from datetime import datetime
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class MongoDB:
    try:
        c = MongoClient(host="localhost", port=27017)
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
    dbh = c["mydb"]
    user_doc = {
    "username" : "janedoe",
    "firstname" : "Jane",
    "surname" : "Doe",
    "dateofbirth" : datetime(1974, 4, 12),
    "email" : "janedoe7s4@example.com",
    "score" : 0
}
    def insert(self):
         dbh.users.insert_one(user_doc)
         print "Successfully inserted document: %s" % user_doc

    def find(self):
         cursor = dbh.users.find()
         for d in cursor:
             print (d)



#if __name__ == "__main__":
#main()
