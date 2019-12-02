from bottle import route, run, get, post, request
from bson.json_util import dumps
import json
import dns
import requests
from src import mongo_connection as mc

@route("/")
def index():
    """To get all the data from the DB"""
    return dumps(coll.find())

@get("/<chat_id>/messages")
def getMessages(chat_id):
    """You can get the list of messages from the chat you select"""
    return dumps(coll.find({'idChat':int(chat_id)}, {"userName":1,"text": 1,"_id":0}))
    

@get("/users")
def getUsers():
    """You can get the list of all the users of the DB with their user_id associated"""
    return dumps(coll.aggregate([{"$group":{"_id": {"idUser":"$idUser", "userName":"$userName"}}}]))

@post('/user/create')
def createuser():
    """You can create a new user to upload to the DB"""
    name = str(request.forms.get("name"))
    new_id = coll.distinct("idUser")[-1] + 1
    new_user = {
        "idUser":new_id,
        "userName":name
    }
    coll.insert_one(new_user)

@post('/chat/<chat_id>/addmessage')
def createMessage(chat_id):
    db1, coll1 = mc.connectCollection('apiproject','chats')
    user = dumps(coll1.find({"idChat":int(chat_id)},{"idUser":1,"userName":1}))
    
    message = str(request.forms.get("message"))
    new_id = coll.distinct("idMessage")[-1] + 1
    new_message = {
        "idUser":idUser,
        "userName": username,
        "idChat": int(chat_id),
        "idMessage":new_id,
        "text" : message
    }
    coll.insert_one(new_message)






db, coll = mc.connectCollection('apiproject', 'chats')
run(host="0.0.0.0", port=8080, debug=True)