from bottle import route, run, get, post, request
from bson.json_util import dumps
import json
import dns
import requests
from src import mongo as m

@route("/total")
def index():
    return dumps(coll.find())

@post('/user/create')
def createuser():
    name = str(request.forms.get("name"))
    new_id = coll.distinct("idUser")[-1] + 1
    new_user = {
        "idUser":new_id,
        "userName":name
    }
    coll.insert_one(new_user)

@post('chat/<chat_id>/addmessage')
def createMessage(chat_id):
    message = str(request.forms.get("message"))
    new_id = coll.distinct("idMessage")[-1] + 1
    new_message = {
        "idChat": chat_id,
        "idMessage":new_id,
        "text" : message
    }
    coll.insert_one(new_message)

db, coll = m.connectCollection('apiproject', 'chats')
run(host="0.0.0.0", port=8080, debug=True)