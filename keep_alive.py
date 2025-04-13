from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot está vivo!", 200

def manter_vivo():
    Thread(target=app.run, kwargs={"host": "0.0.0.0", "port": 8080}).start()
