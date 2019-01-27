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
    json_response = {
        "id": DB.findMatch(content["id"])
    }
    return Response(json.dumps(json_response),mimetype='application/json')

# {otherUserID: [id]
#  currentUserID: [id]           }
@app.route('/add',methods=['POST'])
def addMatch():
    if curr_db.size() == 0:
        return "ERROR:Database is empty"
    content = request.get_json()
    curr_db.add_match(content["currentUserID"],content["otherUserID"])
    return curr_db

# expects request
# {id: [idhere]}
@app.route('/remove',methods=['POST'])
def removeMatch():
    if curr_db.size() == 0:
        return "ERROR:Database is empty"
    curr_db[content["id"]].remove_User_matches()

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

# expects request
# {
#   user ID
#}
@app.route('/deets',methods=['POST'])
def deets():
    content = request.get_json()
    if content == None or content == '':
        return 'No data'
    id = content["id"]
    json_response = {
        "first_name":curr_db[id].first_name,
        "last_name":curr_db[id].last_name,
        "matches":curr_db[id].matches,
        "age":curr_db[id].age,
        "bio":curr_db[id].bio,
        "img":curr_db[id].img,
        "skill":curr_db[id].skill
    }
    return Response(json.dumps(json_response),mimetype='application/json')
if __name__== "__main__":
    app.run(debug=True)

