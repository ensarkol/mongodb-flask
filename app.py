from flask import Flask, jsonify
from pymongo import MongoClient
from bson import json_util
import json
import random

app = Flask(__name__)
client = MongoClient('mongodb://<username>:<password>@<mongo-container-name>:27017/<db_name>') 
db = client['db_name']
collection = db['collection_name']

@app.route('/alldata', methods=['GET'])
def get_data():
    data = []
    i=1
    for item in collection.find():
        data.append({'name': item['ülke']})
    
    return jsonify({'data': data})

@app.route('/staj', methods=['GET'])
def get_random_document():
    count = collection.count_documents({})
    random_index = random.randint(0, count-1)
    random_document = collection.find().limit(-1).skip(random_index).next()
    json_document = json.loads(json_util.dumps(random_document))
    return jsonify(json_document)

@app.route('/')
def index():
    return 'Merhaba Python!'

if __name__ == '__main__':
    app.run(debug=True)
