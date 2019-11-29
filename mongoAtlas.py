from pymongo import MongoClient
import getpass
import json
import os

#Get Password
password = getpass.getpass("Insert your AtlasMongoDB Mohusty password: ")
connection = "mongodb+srv://Mohusty:{}@api-project-6exv8.mongodb.net/test?retryWrites=true&w=majority".format(password)

#Connect to DB
client = MongoClient(connection)
def connectCollection(database, collection):
    db = client[database]
    coll = db[collection]
    return db, coll

db, coll = connectCollection('apiproject','chats')

with open('chats.json') as f:
    chats_json = json.load(f)
coll.insert_many(chats_json)