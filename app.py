from flask import Flask, request
import json
from inference2 import recommend_hotels
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        data = request.data.decode()
        if (data):
            data = json.loads(request.data.decode())
            if ("query" in data):
                return recommend_hotels(json.loads(request.data.decode())['query'])
        return {"msg": "No query provided"}, 400
