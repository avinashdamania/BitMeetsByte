from flask import Flask
from flask import request, request
import random
import User
from DB import DB
app = Flask(__name__)
curr_db = DB()

@app.route('/find',methods=['POST'])
def findMatch():
    if curr_db.size() == 0:
        return "ERROR:Database is empty"
    # pick a match
    index = getMatch()
    user = curr_db.get_user(index)
    # TODO: prevent choosing yourself 
    return user

def getMatch():
    return random.randint(0,curr_db.size())
    
@app.route('/add',methods=['POST'])
def addMatch():
    if curr_db.size() == 0:
        return "ERROR:Database is empty"
    return curr_db

@app.route('/remove',methods=['POST'])
def removeMatch():
    if curr_db.size() == 0:
        return "ERROR:Database is empty"
    return 'Hello, World!'

# expects request
# {name: [namehere]}
@app.route('/new',methods=['POST'])
def newUser():
    content = request.get_json()
    if content == None or content == '':
        return 'No data'
    curr_db.add_user(content['name'])
    return content['name'] +  ' has been added'

@app.route('/bindaddy',methods=['GET'])
def bindaddy():
    return "YAASSSSSSSS BINDADDY"
