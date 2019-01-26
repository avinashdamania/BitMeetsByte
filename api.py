from flask import Flask
from flask import request
import random
import User
from DB import DB

app = Flask(__name__)

user_list = []
curr_db = DB()

@app.route('/find',methods=['GET'])
def findMatch():
    # pick a random person
    # index = random.choice(user_list)
    # chosen_id = user_list[index]
    # TODO: prevent choosing yourself 
    return 'hi'

@app.route('/add',methods=['POST'])
def addMatch():
    return user_list

@app.route('/remove',methods=['POST'])
def removeMatch():
    return 'Hello, World!'

@app.route('/new',methods=['POST'])
def newUser():
    content = request.get_json()
    if content == None or content == '':
        return 'FAILURE!'
    curr_db.add_user(content['name'])
    return 'SUCCESS!'

@app.route('/bindaddy',methods=['GET'])
def addMatch():
    return "YAASSSSSSSS BINDADDY"
