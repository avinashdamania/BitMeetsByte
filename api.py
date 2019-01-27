from flask import Flask
from flask import request, request
import random
import User
from db import DB
app = Flask(__name__)
curr_db = DB()

# {id: [name]}
@app.route('/find',methods=['POST'])
def findMatch():
    if curr_db.size() == 0:
        return "ERROR:Database is empty"
    # pick a match
    index = getMatch()
    user = curr_db.get_user(index)
    # TODO: prevent choosing yourself
    # TODO: add user data when actual matching is used 
    return user

def getMatch():
    return random.randint(0,curr_db.size())

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
        content['misc'])
    return content['first_name'] +  ' has been added'

if __name__== "__main__":
    app.run(debug=True)

