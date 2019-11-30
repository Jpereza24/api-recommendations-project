from pymongo import MongoClient
from bson.json_util import dumps
import json
import os
import dns
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()


password = os.getenv("MONGOURL")
client = MongoClient(password)

def connectCollection(database, collection):
    db = client[database]
    coll = db[collection]
    return db, coll
