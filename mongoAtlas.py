from pymongo import MongoClient
import getpass
import json
import os
from dotenv import load_dotenv
load_dotenv()

#Get Password
password = getpass.getpass("Insert your AtlasMongoDB Mohusty password: ")
connection = os.getenv("mongoURL")

#Connect to DB
client = MongoClient(connection)
def connectCollection(database, collection):
    db = client[database]
    coll = db[collection]
    return db, coll

db, coll = connectCollection('apiproject','chats')

with open('../Input/chats.json') as f:
    chats_json = json.load(f)
coll.insert_many(chats_json)