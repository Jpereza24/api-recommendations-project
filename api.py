from bottle import route, run, get, post, request
from bson.json_util import dumps
import json
import os
import dns
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

password = os.getenv("MONGOURL")
client = MongoClient(password)
db = client['apiproject']
coll = db['chats']

@get("/")
def index():
    return dumps(coll.find())
run(host="127.0.0.1", port=8080)

@post('/createuser/<username>')
def userCreation(username):
    ''' Insertas un username y te devuelve el user_id'''
    return user_id