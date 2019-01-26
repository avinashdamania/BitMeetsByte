from flask import Flask
app = Flask(__name__)

@app.route('/find',methods=['POST'])
def findMatch():
    return 'Hello, World!'

@app.route('/add',methods=['POST'])
def addMatch():
    return 'Hello, World!'

@app.route('/remove',methods=['POST'])
def removeMatch():
    return 'Hello, World!'