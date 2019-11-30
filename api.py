from bottle import route, run, get, post, request
from bson.json_util import dumps
import json
import dns
import requests
from src import mongo as m

@route("/data")
def data():
    return dumps(coll.find())




@post('/createuser/<username>')
#def createuser(username):
    #''' Insertas un username y te devuelve el user_id'''

    #return user_id

db, coll = m.connectCollection('apiproject', 'chats')
run(host="0.0.0.0", port=8080, debug=True)