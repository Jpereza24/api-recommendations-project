@get('/chat/create')
def chatCreation(array):
    '''Crear un chat en el que cargar mensajes, hay que meter un array de user_ids'''
    return chat_id

@get('/chat/<chat_id>/adduser')
def userChat(user_id):
    '''Añade un usuario a un chat'''
    return chat_id