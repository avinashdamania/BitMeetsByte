from flask import Flask
from flask import request, Response
import random
import User
from db import DB
import json
app = Flask(__name__)
curr_db = DB()
curr_db.gen_database()
@app.route('/')
def home():
    return 'hi'

# {id: [name]}
@app.route('/find',methods=['POST'])
def findMatch():
    if curr_db.size() == 0:
        return "ERROR:Database is empty"
    content = request.json()
    return DB.findMatch(content["id"])

# {otherUserID: [id]
#  currentUserID: [id]           }
@app.route('/add',methods=['POST'])
def addMatch():
    if curr_db.size() == 0:
        return "ERROR:Database is empty"
    content = request.get_json()
    matched_user = curr_db.get_user(content['otherUserID'])
    curr_db.add_match(id,matched_user)
    return curr_db

# expects request
# {id: [idhere]}
@app.route('/remove',methods=['POST'])
def removeMatch():
    if curr_db.size() == 0:
        return "ERROR:Database is empty"
    return 'Hello, World!'

# expects request
# {
# first_name: [firstnamehere],
# last_name: [lastnamehere],
# age: [agehere],
# bio: [biohere],
# misc: [mischere],}
@app.route('/new',methods=['POST'])
def newUser():
    content = request.get_json()
    if content == None or content == '':
        return 'No data'
    curr_db.add_user(
        content['first_name'],
        content['last_name'],
        content['age'],
        content['bio'],
        content['img'],
        content['skill'])
    size =  curr_db.size() - 1
    json_response = {
        "id": size
    }
    return Response(json.dumps(json_response),mimetype='application/json')

if __name__== "__main__":
    app.run(debug=True)

