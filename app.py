from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import pymongo
from pymongo import MongoClient

#-------------------------------------------------------------------------------
# Replace these with your server details
MONGO_HOST = os.getenv('MONGODB_HOSTNAME', '127.0.0.1')
MONGO_PORT = os.getenv('MONGODB_PORT', '27017')
MONGO_USER = os.getenv('MONGODB_USERNAME', 'user')
MONGO_PASS = os.getenv('MONGODB_PASSWORD', 'pwd')

uri = "mongodb://{}:{}@{}:{}/".format(MONGO_USER, MONGO_PASS, MONGO_HOST, MONGO_PORT)
conn = MongoClient(uri, connect=False)
db = conn['sega']
#-------------------------------------------------------------------------------

# configuration
DEBUG = True

application = Flask(__name__)

# enable CORS
CORS(application, resources={r'/*': {'origins': '*'}})

BOOKS = [
    {
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

@application.route("/")
def hello_world():
    dbData = db.saturnGameList.find()
    gameNameList = [data['title'] for data in dbData]
    gameNameList = str(gameNameList)
    return gameNameList



# sanity check route
@application.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@application.route('/getList', methods=['GET'])
def getList():
    dbData = db.saturnGameList.find()
    gameNameList = [data['title'] for data in dbData]
    gameNameList = str(gameNameList)
    response = jsonify(gameNameList)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

#  @application.route('/books', methods=['GET'])
#  def all_books():
    #  return jsonify({
        #  'status': 'success',
        #  'books': BOOKS
    #  })

@application.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    response = jsonify(response_object)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


#  if __name__ == '__main__':
    #  app.run()
