from flask import Flask, request, render_template
from datetime import datetime
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = os.getenv('MONGO_URI')

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
#client = MongoClient(uri, ssl=True, tls=True, server_api=ServerApi('1'))
#client = MongoClient(uri, ssl=True, ssl_cert_reqs='CERT_NONE', server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.test

collection = db['flask-tutorial']

app = Flask(__name__)

@app.route('/')
def home():

    day_of_week = datetime.today().strftime('%A')
    current_time = datetime.today().strftime('%H:%M:%S')

    return render_template('index.html', day=day_of_week, time=current_time)


@app.route('/submit', methods=['POST'])
def submit():

    form_data = dict(request.form)

    collection.insert_one(form_data)

    return 'Data Submitted!'

@app.route('/view')
def view():
    
    data = collection.find()

    data = list(data)

    for item in data:
        print(item)

        del item['_id']
    
    data = {
        'data': data
    }

    return data

if __name__ == '__main__':
    app.run(debug=True)