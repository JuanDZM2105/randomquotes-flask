from flask import Flask, jsonify
import os
import random

app = Flask(__name__)

phrases = [
    "La verdadera fuerza es proteger, no destruir", 
    "La verdadera fuerza es proteger, no destruir",
]


@app.route('/')
def get_random_quote():
    phrase = random.choice(phrases)
    container_id = os.uname()[1] 
    return f"{phrase} - Container Id: {container_id}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

