from bottle import route, run, get, post, request,error 
import random
import os

@get("/")
def nombre():
    return {"nombre": random.choice(["Joaquin","Mustafa","tu puta madre"])}

@error(404)
def error404(error):
    return {"error": "mierda"}

port = int(os.getenv("PORT", 8080))
print(f"Running server {port}...")

run(host="0.0.0.0", port=port, debug=True)