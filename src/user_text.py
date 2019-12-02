import re

def user_text(lista):
    users_dict=dict()
    for dicc in lista:
        if dicc['userName'] not in users_dict:
            users_dict[dicc['userName']]=dicc['text']
        else:
            users_dict[dicc['userName']]+=' ' +dicc['text']
    for e in users_dict:
        users_dict[e]=re.sub(r"[^a-zA-Z0-9]+", ' ', users_dict[e])
    return users_dict