from bottle import route, run, get, post, request
from bson.json_util import dumps
import json
import dns
import requests
from src import mongo_connection as mc
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

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

@get("/users/messages")
def userMessages():
    """This function returns all the messages for each user"""
    registro = list(user.aggregate([{'$project':{'userName':1,'_id':0}}]))
    messages_user = []
    for dicc in registro:
        messages_user.append({'userName':dicc['userName'], 'messages': list(coll.find({'userName':dicc['userName']},{'text':1,'_id':0}))})
    return json.dumps(messages_user)

@post('/user/create')
def createuser():
    """You can create a new user to upload to the DB users """
    registro = list(user.aggregate([{'$project':{'userName':1}}]))
    name = str(request.forms.get("name"))
    new_id = max(user.distinct("idUser")) + 1
    new_user = {
        "idUser":new_id,
        "userName":name
    }
    if name in [e['userName'] for e in registro]:
        print("Error! That user is already created")
    else:
        user.insert_one(new_user)
        print(f"New user created with name {name} and id {new_id}")

@post('/chat/<chat_id>/addmessage')
def createMessage(chat_id):
    """This function adds a message to the chat that you choose, also it checks if the person who talks is an existing user or a new user"""
    idUser = max(user.distinct('idUser')) +1
    regis = list(user.aggregate([{'$project':{'userName':1, 'idUser':1,'_id':0}}]))
    name = str(request.forms.get("name"))
    message = str(request.forms.get("message"))
    new_id = max(coll.distinct("idMessage"))+ 1
    for l in regis:
        if l['userName']==name:
            idUser = l['idUser']
    new_message = {
        "idUser":idUser,
        "userName": name,
        "idChat": int(chat_id),
        "idMessage":new_id,
        "text" : message
    }
    new_user = {
        "idUser":idUser,
        "userName":name
    }
    if name not in [e['userName'] for e in regis]:
        user.insert_one(new_user)
    coll.insert_one(new_message)

@get('/<chat_id>/sentiment')
def getSentiment(chat_id):
    """Returns the average sentiments from the messages of a chat"""
    query = list(coll.find({'idChat':int(chat_id)}, {"userName":1,"text": 1,"_id":0}))
    texts = [e['text'] for e in query]
    sid = SentimentIntensityAnalyzer()
    sentiment = [sid.polarity_scores(string) for string in texts]
    average_sentiment = {
        "Average Sentiment in the Chat":{
            "Negativity": sum(e['neg'] for e in sentiment)/len(sentiment),
            "Neutral": sum(e['neu'] for e in sentiment)/len(sentiment),
            "Positivity": sum(e['pos'] for e in sentiment)/len(sentiment),
            "Compound": sum(e['compound'] for e in sentiment)/len(sentiment)
    }}
    return average_sentiment

db, coll = mc.connectCollection('apiproject', 'chats')
datauser, user = mc.connectCollection('apiproject', 'users')
run(host="0.0.0.0", port=8080, debug=True)