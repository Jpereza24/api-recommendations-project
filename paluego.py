@post('/user/create')
def userCreation(username):
    ''' Insertas un username y te devuelve el user_id'''
    return user_id

@get('/chat/create')
def chatCreation(array):
    '''Crear un chat en el que cargar mensajes, hay que meter un array de user_ids'''
    return chat_id

@get('/chat/<chat_id>/adduser')
def userChat(user_id):
    '''Añade un usuario a un chat'''
    return chat_id

@post('/chat/<Chat_id>/addmessage')
def addMessage(chat_id,user_id,message):
    '''Añade un mensaje al chat al que se le indique'''
    return message_id

@get('/chat/<chat_id>/list')
def getMesages(chat_id):
    '''Pones un chat_id y te devuelve una lista con todos los mensajes que ha habido en ese chat'''
    return list_of_messages

@get('chat/<chat_id>/sentiment')
def getSentiment(chat_id):
    '''Pones un chat_id y te devuelve el ratio de sentimientos de los mensajes en ese chat'''
    return sentiment