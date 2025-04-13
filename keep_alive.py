from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot está online!"

def run():
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))

def keep_alive():
    t = threading.Thread(target=run)
    t.start()
