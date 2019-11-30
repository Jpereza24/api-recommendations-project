from bottle import route, run, get, post, request
from bson.json_util import dumps
import json
import os
import dns
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

password = os.getenv('mongoURL')
client = MongoClient(password)
db = client['apiproject']
coll = db['chats']

@get("/")
def index():
    return dumps(coll.find())
run(host="0.0.0.0", port=8080)